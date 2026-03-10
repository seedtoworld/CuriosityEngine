from dataclasses import dataclass
from typing import List

@dataclass
class Page:
    url: str
    title: str
    text: str
    links: List[str]
    domain: str
    depth: int
    content_hash: str = ""