import time
from urllib.parse import urlparse

class DomainLimiter:
    def __init__(self, delay=1.0, max_pages=20):
        self.delay = delay
        self.max_pages = max_pages
        self.last_request = {}
        self.domain_counts = {}

    def allow_crawl(self, url):
        domain = urlparse(url).netloc

        if self.domain_counts.get(domain, 0) > self.max_pages:
            return False
        
        self.domain_counts[domain] = self.domain_counts.get(domain, 0) + 1
        return True


    def wait(self, url):
        domain = urlparse(url).netloc
        last = self.last_request.get(domain)

        if last:
            elapsed = time.time() - last
            if elapsed < self.delay:
                time.sleep(self.delay - elapsed)
        
        self.last_request[domain] = time.time()