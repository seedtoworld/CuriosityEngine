from dataclasses import dataclass

@dataclass
class FrontierItem:
    url: str
    depth: int
    priority: float = 0.0
    source_url: str = ""