from typing import TypedDict
from pathlib import Path
import eyed3  # type: ignore


class TrackInfo(TypedDict):
    """Type for track info."""

    title: str
    artist: str
    album: str
    year: int
    track_number: int


def set_mp3_tags(mp3_file: Path, tags: TrackInfo) -> None:
    """
    Set tags for an MP3 file.

    Args:
        mp3_file (Path): Path to MP3 file.
        tags (TrackInfo): Dictionary containing track info.
    """
    audio_file = eyed3.load(mp3_file)
    if not audio_file:
        return

    audio_file.tag.title = tags["title"]
    audio_file.tag.artist = tags["artist"]
    audio_file.tag.album = tags["album"]
    audio_file.tag.recording_date = eyed3.core.Date(tags["year"])
    audio_file.tag.track_num = tags["track_number"]

    audio_file.tag.save()


def get_mp3_tags(mp3_file: Path) -> TrackInfo | None:
    """
    Get tags of an MP3 file. This includes:
    - Title
    - Artist
    - Album
    - Year
    - Track Number

    Args:
        mp3_file (Path): Path to MP3 file.

    Returns:
        TrackInfo | None: MP3 tags. Returns `None` if unsuccessful.
    """

    audio_file = eyed3.load(mp3_file)
    if not audio_file:
        return None

    audio_track_info: TrackInfo = {
        "title": audio_file.tag.title,
        "artist": audio_file.tag.artist,
        "album": audio_file.tag.album,
        "year": int(str(audio_file.tag.recording_date)),
        "track_number": audio_file.tag.track_num[0],
    }
    return audio_track_info
