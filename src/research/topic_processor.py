import re

# Simple no heavy NLP YET!
class TopicProcessor:

    STOPWORDS = {
        "the","a","an","and","of","to","in","on","for","with","is"
    }

    def extract_keywords(self, topic):
        words = re.findall(r"\w+", topic.lower())

        keywords = [
            w for w in words
            if w not in self.STOPWORDS
        ]

        return keywords