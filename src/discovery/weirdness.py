import re
from urllib.parse import urlparse

class WeirdnessDetector:
    def rare_vocabulary(self, text):
        words = re.findall(r"\b[a-zA-Z]{7,}\b", text.lower())
        if not words:
            return 0
        
        unique = len(set(words))

        return unique / len(words)
    
    def deep_url(self, url):
        path = urlparse(url).path
        depth = path.count("/")
        return min(depth / 10, 1)
    
    def old_structure(self, html):
        indicators = [
            "<font",
            "<center",
            "<frameset",
            "bgcolor="
        ]

        score = 0

        for i in indicators:
            if i in html.lower():
                score += 1
        
        return score / len(indicators)
    
    def unusual_domain(self, url):
        domain = urlparse(url).netloc

        unusual_tlds = [
            ".museum",
            ".science",
            ".space",
            ".arpa"
        ]

        for tld in unusual_tlds:
            if domain.endswith(tld):
                return 1
        
        return 0