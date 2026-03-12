from urllib.parse import urlparse
from collections import Counter

class CuriositySignals:
    def __init__(self):
        self.seen_domains = set()
        self.url_tokens = Counter()
    
    # new sites
    def domain_novelty(self, url):
        domain = urlparse(url).netloc

        if domain not in self.seen_domains:
            self.seen_domains.add(domain)
            return 1.0
        
        return 0.0
    
    # unseen url patterns
    def novelty_score(self, url):
        tokens = url.split("/")
        score = 0

        for t in tokens:
            if self.url_tokens[t] == 0:
                score += 1
            
            self.url_tokens[t] += 1
        
        return score / (len(tokens) + 1)
    
    # rare url tokens
    def rarity_score(self, url):
        tokens = url.split("/")
        rarity = 0

        for t in tokens:
            count = self.url_tokens[t] + 1
            rarity += 1 / count
        
        return rarity / len(tokens)
    
    # exploration
    def depth_bonus(self, depth):
        return depth * 0.1