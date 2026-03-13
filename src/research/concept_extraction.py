import re
from collections import Counter

class ConceptExtractor:
    def extract(self, text, top_k=10):
        words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
        counter = Counter(words)

        return [w for w,_ in counter.most_common(top_k)]