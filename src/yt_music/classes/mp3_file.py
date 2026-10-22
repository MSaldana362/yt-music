from dataclasses import dataclass
from pathlib import Path
import eyed3


@dataclass
class Mp3Tags:
    """Available MP3 file tags."""

    artist: str | None = None
    album: str | None = None
    year: int | None = None
    track_name: str | None = None
    track_number: int | None = None
    genre: str | None = None


class TagError(Exception):
    """Error raised for MP3 tags."""


class Mp3File:
    """MP3 File"""

    def __init__(self, filepath: str | Path):
        filepath = Path(filepath).expanduser()
        if not filepath.is_file():
            raise FileNotFoundError(f"File not found: {filepath}")
        if filepath.suffix.lower() != ".mp3":
            raise ValueError(f"File not an MP3 file: {filepath}")

        self.filepath = filepath.resolve()

        self.audiofile = self._load_audio_file()

    def _load_audio_file(self) -> eyed3.AudioFile:
        """Init audio file."""
        audiofile = eyed3.load(self.filepath)
        if audiofile is None:
            raise ValueError(f"Unable to load audio data: {self.filepath}")

        return audiofile

    @property
    def filename(self) -> str:
        """Name of MP3 file."""
        return self.filepath.stem

    @property
    def parentdir(self) -> Path:
        """Parent directory of MP3 file."""
        return self.filepath.parent

    def rename_to_expected(self) -> None:
        """Rename MP3 file to expected format (`track_number` - `track_name`)."""
        track_name = self.audiofile.tag.title
        track_number = self.audiofile.tag.track_num[0]

        if track_name is None or track_number is None:
            return

        # todo: clean name

        expected = f"{track_number:02d} - {track_name}"
        if self.filepath.stem == expected:
            return

        newpath = self.filepath.rename(self.filepath.with_stem(expected))
        self.filepath = newpath.resolve()
        self.audiofile = self._load_audio_file()

    def set_tags(self, tags: Mp3Tags) -> None:
        """Set tags for MP3 file."""
        try:
            self.audiofile.tag.artist = tags.artist
            self.audiofile.tag.album = tags.album
            self.audiofile.tag.recording_date = eyed3.core.Date(tags.year)
            self.audiofile.tag.title = tags.track_name
            self.audiofile.tag.track_num = tags.track_number
            self.audiofile.tag.genre = tags.genre

            self.audiofile.tag.save()

        except Exception as e:
            raise TagError(f"Failed to set tags for '{self.filepath}': {e}") from e

    def get_tags(self) -> Mp3Tags:
        """Get tags from MP3 file."""

        try:
            return Mp3Tags(
                artist=self.audiofile.tag.artist,
                album=self.audiofile.tag.album,
                year=self.audiofile.tag.recording_date,
                track_name=self.audiofile.tag.title,
                track_number=self.audiofile.tag.track_num[0],
                genre=self.audiofile.tag.genre,
            )

        except Exception as e:
            raise TagError(f"Failed to get tags for '{self.filepath}': {e}") from e

    def apply_album_art(self, artpath: str | Path) -> None:
        """Apply album art for MP3 file."""
        artpath = Path(artpath).expanduser()
        if not artpath.is_file():
            raise FileNotFoundError(f"File not found: {artpath}")

        try:
            with open(artpath, "rb") as img:
                self.audiofile.tag.images.set(
                    eyed3.id3.frames.ImageFrame.FRONT_COVER, img.read(), "image/jpeg"
                )

            self.audiofile.tag.save()

        except Exception as e:
            raise TagError(
                f"Failed to apply album art for '{self.filepath}': {e}"
            ) from e
