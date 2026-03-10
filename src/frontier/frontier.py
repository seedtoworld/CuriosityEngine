from collections import deque

from src.models.frontier_item import FrontierItem
from src.utils.logger import logger

class Frontier:

    def __init__(self, max_size: int = 10000):
        self.queue = deque()

        self.seen_urls = set()
        self.visited_urls = set()

        self.max_size = max_size
    
    def add_url(self, url: str, depth: int):
        if url in self.seen_urls:
            return False
        
        if len(self.queue) >= self.max_size:
            logger.warning("Frontier limit reached!")
            return False
        
        item = FrontierItem(url=url, depth=depth)
        
        self.queue.append(item)
        self.seen_urls.add(url)

        return True
    
    def get_next(self):
        if not self.queue:
            return None
        
        item = self.queue.popleft()

        self.visited_urls.add(item.url)

        return item
    
    def mark_visited(self, url: str):
        self.visited_urls.add(url)
    
    def is_visited(self, url: str):
        return url in self.visited_urls
    
    def size(self):
        return len(self.queue)