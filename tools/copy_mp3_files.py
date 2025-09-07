"""
Copy MP3 files in a sorted order.
"""

import argparse
from pathlib import Path
from typing import List


def is_mp3_dir(user_dir: Path) -> bool:
    """
    Determine if a directory contains MP3 files.
    """

    if not user_dir.exists() or not user_dir.is_dir():
        return False

    for item in user_dir.iterdir():
        if not item.is_file():
            continue

        if item.suffix == ".mp3":
            return True

    return False


def get_mp3_dirs(source_dir: Path) -> List[Path]:
    """
    Return a list of paths to all MP3 directories.
    """

    mp3_dirs: List[Path] = []

    source_dir_files = source_dir.rglob("*")
    for file in source_dir_files:
        if file.is_dir() and is_mp3_dir(file):
            mp3_dirs.append(file)

    return sorted(mp3_dirs)


def copy_mp3_files(source_dir_str: str, target_dir_str: str) -> None:
    """
    Main entry point.
    """
    print(f"{source_dir_str=}")
    print(f"{target_dir_str=}")

    source_dir = Path(source_dir_str)
    target_dir = Path(target_dir_str)

    for user_path in (source_dir, target_dir):
        if not user_path.exists() or not user_path.is_dir():
            print(f"Not a valid directory: {user_path}")
            return

    mp3_dirs = get_mp3_dirs(source_dir=source_dir)
    print(mp3_dirs)


if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(
        description="Copy MP3 files in a sorted order.",
        usage="python -m tools.copy_mp3_files [SOURCE_DIR] [TARGET_DIR]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("source_dir", type=str, help="Source directory.")
    parser.add_argument("target_dir", type=str, help="Target directory.")

    # parse arguments
    args = parser.parse_args()

    copy_mp3_files(source_dir_str=args.source_dir, target_dir_str=args.target_dir)
