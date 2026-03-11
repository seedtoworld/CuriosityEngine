import requests
import time

from src.utils.logger import logger

MAX_RETRIES = 3

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
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(
                    url,
                    timeout=self.timeout
                )

                content_type = response.headers.get("Content-Type", "")
                if "text/html" not in content_type:
                    return None

                logger.info(f"Fetched {url} [{response.status_code}]")

                return {
                    "url": url,
                    "status_code": response.status_code,
                    "html": response.text
                }
            
            except requests.exceptions.Timeout:
                logger.warning(f"Timeout fetching {url}")

            except Exception as e:
                logger.error(f"Failed to fetch {url}: {e}")
        
        logger.error(f"Failed after retries: {url}")

        return None