# simple relevance score
class TopicRelevance:
    def score(self, text, keywords):
        if not keywords:
            return 0

        text = text.lower()

        score = 0

        # topic keywords get stronger weight
        for k in keywords:
            count = text.count(k)
            score += count * 2

        return score