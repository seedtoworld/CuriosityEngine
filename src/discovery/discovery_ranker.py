class DiscoveryRanker:
    def __init__(self, detector):
        self.detector = detector
    
    def score(self, url, text, html):
        vocab = self.detector.rare_vocabulary(text)
        deep = self.detector.deep_url(url)
        old = self.detector.old_structure(html)
        domain = self.detector.unusual_domain(url)

        score = (
            vocab * 0.4 +
            deep * 0.2 +
            old * 0.2 +
            domain * 0.2
        )

        return score