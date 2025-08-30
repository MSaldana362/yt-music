"""
Utils for yt_dlp.
"""

from typing import List, TypedDict
from pathlib import Path
import yt_dlp


class YouTubeInfo(TypedDict):
    """Type for YouTube info"""

    titles: List[str]
    urls: List[str]
    is_playlist: bool


def get_youtube_info(youtube_url: str) -> YouTubeInfo | None:
    """Get info from a YouTube playlist or video. This includes:
    - List of titles
    - List of URLs
    - Boolean indicating if playlist.

    Args:
        youtube_url (str): URL of YouTube playlist or video.

    Raises:
        Exception: _description_
        ValueError: _description_
        KeyError: _description_

    Returns:
        YouTubeInfo | None: YouTube info. Returns `None` if unsuccessful.
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
                    urls = [entry["url"] for entry in entries]

                    playlist_info: YouTubeInfo = {
                        "titles": titles,
                        "urls": urls,
                        "is_playlist": True,
                    }
                    return playlist_info

                case "watch":
                    print("Video".center(100, "-"))
                    print(f"{info['title']}".ljust(50) + f"{info['channel']}")

                    titles = [info["title"]]
                    urls = [info["webpage_url"]]

                    video_info: YouTubeInfo = {
                        "titles": titles,
                        "urls": urls,
                        "is_playlist": False,
                    }
                    return video_info

        except Exception as e:
            raise KeyError(f"Error: Issue encountered while parsing info. {e}") from e

        return None


def download_to_mp3(youtube_url: str, download_dir: Path, file_name: str) -> None:
    """
    Download YouTube video as MP3.
    """

    options = {
        "format": "bestaudio/best",
        "outtmpl": f"{download_dir}/{file_name}.%(ext)s",
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
