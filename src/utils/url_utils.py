from urllib.parse import urlparse, urlunparse

BAD_EXTENSIONS = (
    ".jpg", ".jpeg", ".png", ".gif",
    ".pdf", ".zip", ".rar",
    ".mp4", ".mp3",
    ".svg"
)

def normalize_url(url: str) -> str:
    parsed = urlparse(url)

    cleaned = parsed._replace(
        fragment="",            # removee #section
        query=""                # remove ?query=params
    )   

    return urlunparse(cleaned)

def is_valid_url(url: str) -> bool:
    url_lower = url.lower()

    return not url_lower.endswith(BAD_EXTENSIONS)

def same_domain(url: str, seed_domain: str):
    return urlparse(url).netloc == seed_domain