from pydantic import BaseModel, Field


class Thumbnail(BaseModel):
    url: str
    width: int
    height: int


class ArtistReference(BaseModel):
    name: str
    id: str


class AlbumSearchResult(BaseModel):
    title: str
    result_type: str = Field(alias="type")
    playlist_id: str = Field(alias="playlistId")
    year: str
    artists: list[ArtistReference]
    browse_id: str = Field(alias="browseId")
    thumbnails: list[Thumbnail]

    @property
    def playlist_url(self) -> str:
        return f"https://music.youtube.com/playlist?list={self.playlist_id}"

    @property
    def artwork_url(self) -> str:
        return self.thumbnails[-1].url
