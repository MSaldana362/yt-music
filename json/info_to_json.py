"""Export info provided by yt_dlp as json."""

import json
from typing import TypedDict
import yt_dlp


class YouTubeType(TypedDict):
    name: str
    url: str


def info_to_json(youtube_types: list[YouTubeType]):

    for youtube_type in youtube_types:

        name = youtube_type["name"]
        url = youtube_type["url"]

        if not url:
            print(f"No URL provided for {name}. Skipping.")
            continue

        options = {"extract_flat": True, "playlistend": None}
        with yt_dlp.YoutubeDL(options) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
            except Exception as e:
                raise RuntimeError(f"Error: Failed to extract info. {e}") from e

            output_path = f"json/{name}.json"
            with open(output_path, "w") as f:
                json.dump(info, f, indent=4)


youtube_types: list[YouTubeType] = [
    {
        "name": "youtube_music_album",
        "url": "https://music.youtube.com/playlist?list=OLAK5uy_nXCZ714FRe9Gr96c9Ycuqummnv8W-dfEs",
    },
    {
        "name": "youtube_music_track",
        "url": "https://music.youtube.com/watch?v=K1XT42YQyOg",
    },
    {
        "name": "youtube_playlist",
        "url": "https://youtube.com/playlist?list=PLfIhUmTWHNvYennkxqa19Ds52rn3YWBFH",
    },
    {"name": "youtube_video", "url": "https://youtu.be/KheYW_G0goY"},
]

info_to_json(youtube_types)
