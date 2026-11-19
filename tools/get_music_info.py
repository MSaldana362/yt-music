"""
Get YouTube Music Info
"""

import argparse
import logging

from yt_music.classes.youtube_url import YouTubeUrl

logging.basicConfig(level=logging.INFO)


def print_info(url: str, index: int | None = None) -> None:
    """Print YouTube Music info"""

    youtube_url = YouTubeUrl(url)
    youtube_url.get_info()

    track_number = f"{index:02d}" if index else None
    track_name = youtube_url.track or ""
    album = youtube_url.album or ""
    artists = " & ".join(youtube_url.artists or [""])
    year = str(youtube_url.release_year) or ""

    if track_number:
        print(", ".join(["track_number", "track_name", "album", "artists", "year"]))
        print(", ".join([track_number, track_name, album, artists, year]))
    else:
        print(", ".join(["track_name", "album", "artists", "year"]))
        print(", ".join([track_name, album, artists, year]))


def get_music_info(url: str) -> None:
    """Get YouTube Music info"""

    youtube_url = YouTubeUrl(url)
    youtube_url.get_info()

    playlist_urls = youtube_url.playlist_urls

    if playlist_urls:
        for index, entry in enumerate(playlist_urls, start=1):
            print_info(url=entry, index=index)

    else:
        print_info(url=url)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Get YouTube Music info",
        usage="python -m tools.get_music_info --help",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("url", type=str, help="URL of YouTube Music")

    args = parser.parse_args()

    get_music_info(url=args.url)
