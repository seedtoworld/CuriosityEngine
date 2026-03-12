from src.engine.signals import CuriositySignals

class CuriosityScorer:
    def __init__(self):
        self.signals = CuriositySignals()
    
    def score(self, url, depth):
        novelty = self.signals.novelty_score(url)
        rarity = self.signals.rarity_score(url)
        domain = self.signals.domain_novelty(url)
        depth_bonus = self.signals.depth_bonus(depth)

        score = (
            novelty * 0.4 +
            rarity * 0.3 +
            domain * 0.2 +
            depth_bonus * 0.1
        )

        return score