from src.crawler.fetcher import Fetcher
from src.parser.html_parser import HTMLParser
from src.utils.url_utils import normalize_url
from src.utils.logger import logger

def crawl(url: str):
    fetcher = Fetcher()
    parser = HTMLParser()

    page = fetcher.fetch(url)

    if not page:
        return

    html = page["html"]

    title = parser.parse_title(html)

    logger.info(f"Page Title: {title}")

    links = parser.extract_links(html, url)

    logger.info(f"Discovered {len(links)} links")

    for link in links[:20]:
        normalized = normalize_url(link)
        print(normalized)

if __name__ == "__main__":
    seed_url = "https://news.ycombinator.com"
    crawl(seed_url)

# https://news.ycombinator.com