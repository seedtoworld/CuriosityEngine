import time
from urllib.parse import urlparse

class DomainRateLimiter:
    def __init__(self, delay=1.0):
        self.delay = delay
        self.last_request = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last = self.last_request.get(domain)

        if last:
            elapsed = time.time() - last
            if elapsed < self.delay:
                time.sleep(self.delay - elapsed)
        
        self.last_request[domain] = time.time()