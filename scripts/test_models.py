from src.models import Page
from src.utils.logger import logger

page = Page(
    url="https://example.com",
    title="Example Title",
    text="Example text",
    links=["https://test.com"],
    domain="example.com",
    depth=10
)

logger.info(f"Created page: {page}")