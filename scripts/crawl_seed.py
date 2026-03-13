import sys

from src.research.topic_processor import TopicProcessor
from src.crawler.fetcher import Fetcher
from src.parser.html_parser import HTMLParser
from src.utils.url_utils import normalize_url, is_valid_url
from src.storage.repository import Repository
from src.engine.scorer import CuriosityScorer
from src.research.relevance import TopicRelevance
from src.research.concept_extraction import ConceptExtractor
from src.research.knowledge_graph import KnowledgeGraph
from src.utils.logger import logger
from src.utils.robots import RobotsManager
from src.utils.rate_limiter import DomainRateLimiter
from src.utils.hash_utils import content_hash

topic = None
keywords = []

def crawl(url: str):
    fetcher = Fetcher()
    parser = HTMLParser()
    repo = Repository()
    robots = RobotsManager()
    rate_limiter = DomainRateLimiter()
    scorer = CuriosityScorer()
    relevance_engine = TopicRelevance()
    concept_extractor = ConceptExtractor()
    knowledge_graph = KnowledgeGraph(repo)

    repo.add_frontier(seed_url, depth=0)

    while True:
        item = repo.get_next_frontier()
        if not item:
            logger.info("Frontier empty. Crawling finished.")

        url = item["url"]
        depth = item["depth"]

        # respect robots.txt
        if not robots.allowed(url, "CuriosityEngine/0.1"):
            logger.info(f"Blocked by robots.txt: {url}")
            continue

        # rate limiting per domain
        rate_limiter.wait(url)

        logger.info(f"Crawling depth={depth} url={url}")

        page = fetcher.fetch(url)
        if not page:
            logger.info(f"Page not found: {url}")
            continue
        
        html = page["html"]
        title = parser.parse_title(html)
        links = parser.extract_links(html, url)
        text = parser.extract_page_text(html)
        hash_value = content_hash(text)

        # [TODO: Replace hashing with storing the visited URLs for duplication detection]
        # Detect duplicate content
        if repo.page_exists(hash_value):
            logger.info(f"Duplicate Content Found: Skipping : {url}")
            continue
        
        # calculate topic relevancd score
        relevance = relevance_engine.score(text, keywords)

        # knowledge graphs
        concepts = concept_extractor.extract(text)
        knowledge_graph.update(concepts)

        repo.save_page(url, title, page["status_code"], text, hash_value)
        repo.save_links(url, links)

        for link in links:
            normalized = normalize_url(link)

            if not is_valid_url(normalized):
                continue
            
            anchor_text = link.get_text().lower()
            anchor_score = relevance_engine.score(anchor_text, keywords)
            curiosity_score = scorer.score(normalized, depth + 1)
            
            score = curiosity_score + relevance + anchor_score
            repo.save_curiosity_scores(url, score)
            repo.add_frontier(normalized, depth + 1, score)
        
        logger.info(f"Discovered {len(links)} links")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        topic = sys.argv[1]
        processor = TopicProcessor()
        keywords = processor.extract_keywords(topic)
    
    seed_url = "https://en.wikipedia.org/wiki/Astronomy"
    crawl(seed_url)

# https://news.ycombinator.com