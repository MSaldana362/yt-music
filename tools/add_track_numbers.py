"""
Add Track Numbers to MP3 Files
"""

import argparse
import logging
from pathlib import Path

from yt_music.classes.mp3_file import Mp3File

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def add_track_numbers(src_dir: str) -> None:
    """Add track numbers to MP3 files"""

    dirpath = Path(src_dir)
    if not dirpath.exists():
        logger.error("Path does not exist: %s", dirpath)
    if not dirpath.is_dir():
        logger.error("Path is not a directory: %s", dirpath)

    for item in dirpath.iterdir():
        if item.is_dir():
            continue
        if item.suffix != ".mp3":
            continue

        logger.info("Found MP3 file: %s", item.name)

        m = Mp3File(item)
        m.rename_for_album()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Add track numbers to MP3 files",
        usage="python -m tools.add_track_numbers --help",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("src_dir", type=str, help="Directory with MP3 files")

    args = parser.parse_args()

    add_track_numbers(src_dir=args.src_dir)
