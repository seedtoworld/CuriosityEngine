from src.crawler.fetcher import Fetcher
from src.parser.html_parser import HTMLParser
from src.utils.url_utils import normalize_url, is_valid_url
from src.frontier.frontier import Frontier
from src.utils.logger import logger

import time

def crawl(url: str):
    fetcher = Fetcher()
    parser = HTMLParser()
    frontier = Frontier()

    frontier.add_url(seed_url, depth=0)

    while frontier.size() > 0:
        item = frontier.get_next()

        url = item.url
        depth = item.depth

        logger.info(f"Crawling depth={depth} url={url}")

        page = fetcher.fetch(url)

        if not page:
            return

        html = page["html"]

        links = parser.extract_links(html, url)

        for link in links:
            normalized = normalize_url(link)

            if not is_valid_url(normalized):
                continue
                
            frontier.add_url(normalized, depth + 1)
        
        logger.info(f"Frontier size: {frontier.size()}")
        
        time.sleep(0.1)

if __name__ == "__main__":
    seed_url = "https://news.ycombinator.com"
    crawl(seed_url)

# https://news.ycombinator.com