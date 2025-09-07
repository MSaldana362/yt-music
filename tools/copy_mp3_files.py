"""
Copy MP3 files in a sorted order.
"""

import argparse
import shutil
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

    sorted_mp3_dirs = sorted(mp3_dirs)

    print(f"Total MP3 Folders Found: {len(sorted_mp3_dirs)}")
    for mp3_dir in sorted(sorted_mp3_dirs):
        print(f"\tFolder: {mp3_dir.name}")

    return sorted_mp3_dirs


def copy_file(source_file: Path, target_file: Path) -> None:
    """
    Copy file. If it exists, touch it.
    """

    if target_file.exists():
        target_file.touch(exist_ok=True)
        print(f"\t\tFile exists. Touched: {target_file.name}")
    else:
        shutil.copy2(source_file, target_file)
        print(f"\t\tCopied: {target_file.name}")


def copy_dir_files(source_mp3_dir: Path, target_mp3_dir: Path) -> None:
    """
    Copy all files from the source directory to the target directory.
    Creates the target directory if it does not exist.
    All files are sorted. MP3 files are copied first.
    """

    print(f"\tSource: {source_mp3_dir}")
    print(f"\tTarget: {target_mp3_dir}")

    if not target_mp3_dir.exists():
        target_mp3_dir.mkdir(parents=True)
        print(f"\t\tCreated Folder: {target_mp3_dir}")

    mp3_files: List[Path] = []
    other_files: List[Path] = []

    source_dir_files = source_mp3_dir.rglob("*")
    for source_file in source_dir_files:
        if not source_file.is_file():
            print(f"Not a file. Skipping: {source_file}")
            continue

        if source_file.suffix.lower() == ".mp3":
            mp3_files.append(source_file)
        else:
            other_files.append(source_file)

    sorted_mp3_files = sorted(mp3_files)
    for source_file in sorted_mp3_files:
        target_file = target_mp3_dir / source_file.name
        copy_file(source_file=source_file, target_file=target_file)

    sorted_other_files = sorted(other_files)
    for source_file in sorted_other_files:
        target_file = target_mp3_dir / source_file.name
        copy_file(source_file=source_file, target_file=target_file)


def copy_mp3_files(source_dir_str: str, target_dir_str: str) -> None:
    """
    Main entry point.
    """

    source_dir = Path(source_dir_str)
    target_dir = Path(target_dir_str)

    for user_path in (source_dir, target_dir):
        if not user_path.exists() or not user_path.is_dir():
            print(f"Not a valid directory: {user_path}")
            return

    mp3_dirs = get_mp3_dirs(source_dir=source_dir)

    total_mp3_dirs = len(mp3_dirs)
    for index, mp3_dir in enumerate(mp3_dirs, start=1):
        print(f"Copying {index} of {total_mp3_dirs}: {mp3_dir.name}")

        relative_path = mp3_dir.relative_to(source_dir)
        target_mp3_dir = target_dir / relative_path

        copy_dir_files(source_mp3_dir=mp3_dir, target_mp3_dir=target_mp3_dir)


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
