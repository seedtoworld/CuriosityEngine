from dataclasses import dataclass
from datetime import datetime

@dataclass
class Discovery:
    url: str
    title: str
    curiosity_score: float
    reason: str
    discovered_at: datetime