from itertools import combinations

class KnowledgeGraph:
    def __init__(self, repo):
        self.repo = repo
    
    def update(self, concepts):
        for c in concepts:
            self.repo.add_concept(c)
        
        for a, b in combinations(concepts, 2):
            self.repo.add_relationship(a, b)
    
    def export_graph(self):
        pass