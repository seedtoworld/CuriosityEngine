from bs4 import BeautifulSoup
from urllib.parse import urljoin

class HTMLParser:

    def parse_title(self, html: str):
        soup = BeautifulSoup(html, "html.parser")

        if soup.title is not None:
            return soup.title.string.strip()
        
        return None
    
    def extract_page_text(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator=" ")
        
        return text
    
    def extract_links(self, html: str, base_url: str):
        soup = BeautifulSoup(html, "html.parser")

        links = []

        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            absolute = urljoin(base_url, href)
            links.append(absolute)
        
        return links