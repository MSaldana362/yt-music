import argparse
from typing import Optional


def download_mp3(
    youtube_url: str, artist: str, album: str, year: int, single: Optional[bool] = False
) -> None:
    """
    Main entry point.
    """
    print(f"{youtube_url=} {artist=} {album=} {year=} {single=}")


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
