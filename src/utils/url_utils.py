from urllib.parse import urlparse, urlunparse

def normalize_url(url: str) -> str:
    parsed = urlparse(url)

    # remove fragments
    cleaned = parsed._replace(fragment="")

    return urlunparse(cleaned)