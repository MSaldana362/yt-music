from pydantic import BaseModel


class YouTubeInfo(BaseModel):
    id: str
    title: str
    webpage_url: str
    original_url: str
    webpage_url_basename: str


class YouTubeMusicTrackInfo(YouTubeInfo):
    album: str
    artists: list[str]
    track: str
    release_year: int


class YouTubeMusicAlbumEntry(BaseModel):
    title: str
    url: str


class YouTubeMusicAlbumInfo(YouTubeInfo):
    entries: list[YouTubeMusicAlbumEntry]
