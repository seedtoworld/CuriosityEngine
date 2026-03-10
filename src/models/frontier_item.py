from dataclasses import dataclass

@dataclass(order=True)
class FrontierItem:
    priority: float
    url: str
    depth: int
    source_url: str