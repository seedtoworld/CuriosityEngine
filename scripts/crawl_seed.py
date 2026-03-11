from src.crawler.fetcher import Fetcher
from src.parser.html_parser import HTMLParser
from src.utils.url_utils import normalize_url, is_valid_url
from src.storage.repository import Repository
from src.utils.logger import logger
from src.utils.robots import RobotsManager
from src.utils.rate_limiter import DomainRateLimiter
from src.utils.hash_utils import content_hash

def crawl(url: str):
    fetcher = Fetcher()
    parser = HTMLParser()
    repo = Repository()
    robots = RobotsManager()
    rate_limiter = DomainRateLimiter()

    repo.add_frontier(seed_url, depth=0)

    while True:
        item = repo.get_next_frontier()
        if not item:
            logger.info("Frontier empty. Crawling finished.")

        url = item["url"]
        depth = item["depth"]

        logger.info(f"Crawling depth={depth} url={url}")

        # respect robots.txt
        if not robots.allowed(url, "CuriosityEngine/0.1"):
            logger.info(f"Blocked by robots.txt: {url}")
            continue

        # rate limiting per domain
        rate_limiter.wait(url)

        page = fetcher.fetch(url)

        if not page:
            continue

        html = page["html"]
        title = parser.parse_title(html)
        links = parser.extract_links(html, url)
        hash_value = content_hash(html)

        # Detect duplicate content
        if repo.page_exists(hash_value):
            continue

        repo.save_page(url, title, page["status_code"], html, hash_value)
        repo.save_links(url, links)

        for link in links:
            normalized = normalize_url(link)

            if not is_valid_url(normalized):
                continue
                
            repo.add_frontier(normalized, depth + 1)
        
        logger.info(f"Discovered {len(links)} links")
    print("Exiting")

if __name__ == "__main__":
    seed_url = "https://news.ycombinator.com"
    crawl(seed_url)

# https://news.ycombinator.com