import requests
from src.utils.logger import logger

class Fetcher:

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": (
                "CuriosityEngine/0.1"
                "(Autonomous curiosity crawler; contact: seedtoworld.dev@gmail.com)"
            )
        })
    
    def fetch(self, url: str):
        try:
            response = self.session.get(
                url,
                timeout=self.timeout
            )

            logger.info(f"Fetched {url} [{response.status_code}]")

            return {
                "url": url,
                "status_code": response.status_code,
                "html": response.text
            }
        
        except Exception as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None