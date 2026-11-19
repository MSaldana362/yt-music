from PySide6.QtCore import QThread, Signal

from yt_music.downloader import downloader


class DownloadWorker(QThread):
    success = Signal()
    failure = Signal()

    def __init__(
        self,
        url: str,
        artist: str,
        album: str,
        year: int,
        art: str | None = None,
        genre: str | None = None,
    ):
        super().__init__()

        self._url = url
        self._artist = artist
        self._album = album
        self._year = year
        self._art = art
        self._genre = genre

    def run(self):
        try:
            downloader(
                url=self._url,
                artist=self._artist,
                album=self._album,
                year=self._year,
                art=self._art,
                genre=self._genre,
            )
        except Exception:
            self.failure.emit()
        else:
            self.success.emit()
