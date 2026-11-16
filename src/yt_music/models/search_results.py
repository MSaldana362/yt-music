from typing import Annotated, Literal

from pydantic import BaseModel, Field, TypeAdapter


class Thumbnail(BaseModel):
    url: str
    width: int
    height: int


class ArtistReference(BaseModel):
    name: str
    id: str | None = None


class AlbumReference(BaseModel):
    name: str
    id: str | None = None


class SearchResult(BaseModel):
    result_type: str = Field(alias="resultType")
    title: str
    year: str | None = None
    artists: list[ArtistReference]
    thumbnails: list[Thumbnail]

    @property
    def artists_str(self) -> str:
        return " & ".join(artist.name for artist in self.artists)

    @property
    def artwork_url(self) -> str:
        return self.thumbnails[-1].url


class AlbumSearchResult(SearchResult):
    result_type: Literal["album"] = Field(alias="resultType")
    playlist_id: str = Field(alias="playlistId")

    @property
    def playlist_url(self) -> str:
        return f"https://music.youtube.com/playlist?list={self.playlist_id}"


class SongSearchResult(SearchResult):
    result_type: Literal["song"] = Field(alias="resultType")
    album: AlbumReference
    video_id: str = Field(alias="videoId")

    @property
    def album_str(self) -> str:
        return self.album.name

    @property
    def song_url(self) -> str:
        return f"https://music.youtube.com/watch?v={self.video_id}"


AnySearchResult = Annotated[
    AlbumSearchResult | SongSearchResult, Field(discriminator="result_type")
]

search_adapter = TypeAdapter(AnySearchResult)
