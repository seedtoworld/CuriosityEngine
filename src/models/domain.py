from dataclasses import dataclass

@dataclass
class Domain:
    name: str
    last_crawled: float
    crawl_delay: float