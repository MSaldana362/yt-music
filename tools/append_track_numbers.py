"""
Append Track Numbers.
"""

import argparse
from pathlib import Path
from typing import List
from utils.tag_utils import get_mp3_tags, TrackInfo


def rename_mp3_file(file_path: Path, tags: TrackInfo) -> None:
    """
    Rename an mp3 file with the track number appended to the beginning of the file name.
    """

    track_title = tags["title"]
    track_number = tags["track_number"]

    old_file_stem = file_path.stem
    if old_file_stem != track_title:
        print(
            f"Track name tag '{track_title}' does not match file name '{old_file_stem}'. Skipping."
        )
        return

    new_file_name = f"{track_number:02d} - {track_title}{file_path.suffix}"
    new_file_path = file_path.parent / Path(new_file_name)

    if new_file_path.exists():
        print(f"File '{new_file_name}' already exists. Skipping.")
        return

    old_file_name = file_path.name
    try:
        file_path.rename(new_file_path)
        print(f"Successfully renamed '{old_file_name}' to '{new_file_name}'.")
    except Exception as e:
        print(f"Something went wrong when renaming '{old_file_name}': {e}")


def append_track_numbers(source_dir: str) -> None:
    """
    Main entry point.
    """

    music_dir_path = Path(source_dir)
    if (not music_dir_path.exists()) or (not music_dir_path.is_dir()):
        print(f"'{music_dir_path.name}' does not exist or is not a valid directory.")

    mp3_file_paths: List[Path] = []
    for item in music_dir_path.iterdir():
        if item.is_file() and item.suffix == ".mp3":
            mp3_file_paths.append(item)

    for mp3_file_path in mp3_file_paths:

        mp3_tags = get_mp3_tags(mp3_file=mp3_file_path)
        if mp3_tags is None:
            print(f"One or more music tags missing from file '{mp3_file_path.name}'.")
            continue

        rename_mp3_file(file_path=mp3_file_path, tags=mp3_tags)


if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(
        description="Appends track numbers to the beginning of music track file names "
        "in a given directory. Music tracks must have metadata already set.",
        usage="python -m tools.append_track_numbers.py [SOURCE_DIR]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("source_dir", type=str, help="Directory with music tracks.")

    # parse arguments
    args = parser.parse_args()

    append_track_numbers(source_dir=args.source_dir)
