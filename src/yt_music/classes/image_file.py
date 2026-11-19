from pathlib import Path
from urllib.parse import urlparse
import logging
import requests

logger = logging.getLogger(__name__)


class ImageFile:
    """Image File"""

    def __init__(self, url: str):
        if not self._validate_url(url):
            raise ValueError(f"Invalid URL: '{url}'")

        self.url = url

    def _validate_url(self, url: str) -> bool:
        try:
            result = urlparse(url)
        except ValueError:
            return False

        return result.scheme in ("http", "https")

    def download(self, dirpath: Path, filename: str) -> Path:
        """Download image file and return path."""
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()

        path = dirpath / f"{filename}.jpg"
        path.write_bytes(response.content)

        logger.info("Image file saved to '%s'", path.name)
        return path
