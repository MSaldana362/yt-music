"""
Clean File Names
"""

import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

INVALID_CHARS = set('<>:"/\\|?*')

REPLACEMENTS = {
    "/": " ",
    ":": "",
    "\\": " ",
    "<": "",
    ">": "",
    '"': "'",
    "|": "-",
    "?": "",
    "*": "",
}

TRANSLATION_TABLE = str.maketrans(REPLACEMENTS)


def _find_invalid_chars(filename: str) -> set[str]:
    return INVALID_CHARS & set(filename)


def _has_invalid_chars(filename: str) -> bool:
    return bool(_find_invalid_chars(filename))


def _clean_name(filename: str) -> str:
    return filename.translate(TRANSLATION_TABLE)


def clean_file_names(src_dir: str | Path, dry_run: bool = False) -> None:
    """Clean file names"""

    dirpath = Path(src_dir)
    if not dirpath.exists():
        logger.error("Path does not exist: %s", dirpath)
    if not dirpath.is_dir():
        logger.error("Path is not a directory: %s", dirpath)

    for item in dirpath.iterdir():
        if item.is_dir():
            clean_file_names(src_dir=item, dry_run=dry_run)

        if not _has_invalid_chars(item.name):
            continue

        oldname = item.name
        newname = _clean_name(item.name)

        newpath = item.with_name(newname)
        if newpath.exists():
            logger.error(
                "File ('%s') with clean name already exists for '%s'", newname, oldname
            )
            continue

        if dry_run:
            logger.info("Would rename '%s' as '%s'", oldname, newname)
        else:
            item.rename(newpath)
            logger.info("Renamed '%s' to '%s'", oldname, newname)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Clean file names",
        usage="python -m tools.clean_file_names --help",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("src_dir", type=str, help="Directory with files")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run")

    args = parser.parse_args()

    clean_file_names(src_dir=args.src_dir, dry_run=args.dry_run)
