from typing import Literal
from pydantic import BaseModel


class YouTubeInfo(BaseModel):
    """YouTube Info"""

    id: str
    title: str
    webpage_url: str
    original_url: str
    webpage_url_basename: str


class YouTubeVideoInfo(YouTubeInfo):
    """YouTube Video Info"""

    webpage_url_basename: Literal["watch"]


class YouTubeMusicTrackInfo(YouTubeInfo):
    """YouTube Music Track Info"""

    webpage_url_basename: Literal["watch"]
    album: str
    artists: list[str]
    track: str
    release_year: int


class YouTubePlaylistEntry(BaseModel):
    """YouTube Playlist Entry"""

    title: str
    url: str


class YouTubePlaylistInfo(YouTubeInfo):
    """YouTube Playlist Info"""

    webpage_url_basename: Literal["playlist"]
    entries: list[YouTubePlaylistEntry]
