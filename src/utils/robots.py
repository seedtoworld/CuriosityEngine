import urllib.robotparser
from urllib.parse import urlparse

class RobotsManager:

    def __init__(self):
        self.parsers = {}
    
    def allowed(self, url, user_agent):
        domain = urlparse(url).netloc

        if domain not in self.parsers:
            robots_url = f"https://{domain}/robots.txt"

            parser = urllib.robotparser.RobotFileParser()
            parser.set_url(robots_url)

            try:
                parser.read()
            except:
                return True
            
            self.parsers[domain] = parser
        
        parser = self.parsers[domain]

        return parser.can_fetch(user_agent, url)