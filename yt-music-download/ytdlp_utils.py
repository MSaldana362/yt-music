"""
Utils for yt_dlp.
"""

from typing import List
from pathlib import Path
import yt_dlp


def get_youtube_titles(youtube_url: str) -> List[str] | None:
    """Get titles from a YouTube playlist or video.

    Args:
        youtube_url (str): URL of YouTube playlist or video.

    Raises:
        Exception: _description_
        ValueError: _description_
        KeyError: _description_

    Returns:
        List[str] | None: Returns a list of YouTube video titles.
    """
    options = {"extract_flat": True, "playlistend": None}

    with yt_dlp.YoutubeDL(options) as ydl:
        # extract info from url
        try:
            info = ydl.extract_info(youtube_url, download=False)
        except Exception as e:
            raise RuntimeError(f"Error: Failed to extract info. {e}") from e

        # verify info exists
        if not info:
            raise ValueError("Error: No info found.")

        # parse info to extract titles
        try:
            match info["webpage_url_basename"]:
                case "playlist":
                    print("Playlist".center(100, "-"))
                    entries = info["entries"]
                    for index, item in enumerate(entries):
                        print(
                            f"{index+1:02d}".ljust(5)
                            + f"{item['title']}".ljust(50)
                            + f"{item['channel']}"
                        )

                    titles = [entry["title"] for entry in entries]
                    return titles

                case "watch":
                    print("Video".center(100, "-"))
                    print(f"{info['title']}".ljust(50) + f"{info['channel']}")

                    titles = [info["title"]]
                    return titles

        except Exception as e:
            raise KeyError(f"Error: Issue encountered while parsing info. {e}") from e

        return None


def download_to_mp3(youtube_url: str, download_dir: Path) -> None:
    """
    Download YouTube playlist or video as MP3.
    """

    options = {
        "format": "bestaudio/best",
        "outtmpl": f"{download_dir}/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "noplaylist": False,
        "ignoreerrors": True,
        # "cookies": "cookies.txt",
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([youtube_url])
