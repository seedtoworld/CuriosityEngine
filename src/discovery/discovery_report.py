class DiscoveryReport:
    def __init__(self, repo):
        self.repo = repo
    
    def generate(self):
        discoveries = self.repo.get_top_discoveries()
        report = []

        for url, score in discoveries:
            report.append({
                "url": url,
                "score": score
            })
        
        return report