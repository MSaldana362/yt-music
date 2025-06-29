# https://ytmusicapi.readthedocs.io/en/latest/

import argparse
from pathlib import Path
from typing import Optional, List
from ytdlp_utils import get_youtube_titles, download_to_mp3
from tag_utils import TrackInfo, set_mp3_tags


def init_music_dir(artist: str, album: str, year: int) -> Path:
    """
    Initializes a directory for the album or single if one does not exist.
    Directory name is in the format '[ARTIST] - [ALBUM] ([YEAR])'.
    Returns the path.
    """

    dir_name = f"{artist} - {album} ({year})"

    music_dir_path = Path(dir_name)
    if not music_dir_path.exists():
        print(f"Creating new directory: '{music_dir_path}'")
        music_dir_path.mkdir()

    return music_dir_path


def create_info_txt(music_dir_path: Path, youtube_url: str, tracks: List[str]) -> None:
    """
    Create TXT file with information about downloaded content.
    """

    info_txt_path = music_dir_path / Path("info.txt")
    print(f"Creating new text file: '{info_txt_path}'")

    info_file = open(info_txt_path, "w")

    info_file.write(f"{music_dir_path.name}\n")
    info_file.write(f"{youtube_url}\n")

    info_file.write("\n" + "Tracks".center(20, "-") + "\n")
    for index, item in enumerate(tracks):
        info_file.write(f"{index+1:02d}".ljust(5) + f"{item}" + "\n")

    info_file.close()


def set_track_tags(
    music_dir_path: Path, tracks: List[str], artist: str, album: str, year: int
) -> None:
    """
    Set tags for all tracks in a directory.
    """
    for index, item in enumerate(tracks):
        track_number = index + 1
        track_title = item

        # build path for track
        track_path = music_dir_path / Path(f"{track_title}.mp3")

        # set tag if file exists
        if track_path.exists():
            track_info: TrackInfo = {
                "title": track_title,
                "track_number": track_number,
                "artist": artist,
                "album": album,
                "year": year,
            }
            set_mp3_tags(mp3_file=track_path, tags=track_info)
        else:
            print(f"Track {track_title} does not exist!")


def download_mp3(
    youtube_url: str, artist: str, album: str, year: int, single: Optional[bool] = False
) -> None:
    """
    Main entry point.
    """

    print(f"{youtube_url=} {artist=} {album=} {year=} {single=}")

    tracks = get_youtube_titles(youtube_url=youtube_url)
    if tracks is None:
        return

    music_dir_path = init_music_dir(artist=artist, album=album, year=year)

    create_info_txt(
        music_dir_path=music_dir_path, youtube_url=youtube_url, tracks=tracks
    )

    download_to_mp3(youtube_url=youtube_url, download_dir=music_dir_path)

    set_track_tags(
        music_dir_path=music_dir_path,
        tracks=tracks,
        artist=artist,
        album=album,
        year=year,
    )


if __name__ == "__main__":
    # set up argument parser
    parser = argparse.ArgumentParser(
        description="Download a playlist or video from YouTube as a music album or single.",
        usage="python download_mp3.py [YOUTUBE_URL] [ARTIST] [ALBUM] [YEAR] [--single]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "youtube_url", type=str, help="URL of the YouTube playlist or video."
    )
    parser.add_argument(
        "artist", type=str, help="The artist name of the album or single."
    )
    parser.add_argument("album", type=str, help="The album or single title.")
    parser.add_argument("year", type=int, help="The year of the album or single.")
    parser.add_argument(
        "--single", action="store_true", help="Download single MP3 file."
    )

    # parse arguments
    args = parser.parse_args()

    download_mp3(
        youtube_url=args.youtube_url,
        artist=args.artist,
        album=args.album,
        year=args.year,
        single=args.single,
    )
