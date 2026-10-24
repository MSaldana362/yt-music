from pathlib import Path
from typing import Any
import logging
import yt_dlp
from pydantic import ValidationError
from yt_music.models.youtube_info import YouTubeInfo, YouTubePlaylistInfo

logger = logging.getLogger(__name__)


class YouTubeUrlException(Exception):
    pass


class YouTubeUrl:

    DEFAULT_OPTIONS: dict[str, Any] = {
        "js_runtimes": {"node": {}},
    }

    def __init__(self, url: str):
        self.url = url
        self._info = None

    def get_info(
        self, quiet: bool = True, no_warnings: bool = True, extract_flat: bool = True
    ) -> dict[str, Any] | None:
        """
        Extract info from a YouTube URL.

        Args:
            quiet (bool, optional): _description_. Defaults to True.
            no_warnings (bool, optional): _description_. Defaults to True.

        Returns:
            dict[str, Any]: _description_
        """

        if self._info is not None:
            return self._info

        options = {
            **self.DEFAULT_OPTIONS,
            "quiet": quiet,
            "no_warnings": no_warnings,
            "extract_flat": extract_flat,
        }

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                info = ydl.extract_info(self.url, download=False)
                if info is None:
                    raise YouTubeUrlException(f"No info returned for {self.url}")
                self._info = ydl.sanitize_info(info)
        except Exception as e:
            raise YouTubeUrlException(
                f"Failed to extract info for {self.url}: {e}"
            ) from e

        return self._info

    def title(self) -> str:
        """Title of playlist or video."""

        try:
            info = YouTubeInfo.model_validate(self._info)
        except ValidationError as e:
            raise ValueError(
                f"YouTube video or playlist has no title: {self.url}"
            ) from e

        return info.title

    def playlist_urls(self) -> list[str]:
        """URLs of playlist entries (if playlist)."""

        try:
            info = YouTubePlaylistInfo.model_validate(self._info)
        except ValidationError:
            logger.info("No entries found for URL: %s", self.url)
            return []

        return [entry.url for entry in info.entries]

    def playlist_titles(self) -> list[str]:
        """Titles of playlist entries (if playlist)."""

        try:
            info = YouTubePlaylistInfo.model_validate(self._info)
        except ValidationError:
            logger.info("No entries found for URL: %s", self.url)
            return []

        return [entry.title for entry in info.entries]

    def _download(
        self, options: dict[str, Any], outpath: Path, max_retries: int
    ) -> bool:
        """Download a YouTube video with options."""

        for attempt in range(max_retries):
            logger.info("Attempt %d of %d", attempt, max_retries)

            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([self.url])
            if outpath.exists():
                return True

            logger.info("Attempt %d failed", attempt)

        return False

    def download_to_mp3(
        self,
        dirpath: str | Path,
        filename: str,
        noplaylist: bool = False,
        ignoreerrors: bool = True,
        max_retries: int = 3,
    ) -> bool:
        """Download a YouTube video as MP3."""

        options = {
            **self.DEFAULT_OPTIONS,
            "format": "bestaudio/best",
            "outtmpl": f"{dirpath}/{filename}.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "noplaylist": noplaylist,
            "ignoreerrors": ignoreerrors,
        }

        outpath = Path(dirpath) / f"{filename}.mp3"
        return self._download(options=options, outpath=outpath, max_retries=max_retries)

    def download_to_mp4(
        self,
        dirpath: str | Path,
        filename: str,
        height: int,
        noplaylist: bool = False,
        ignoreerrors: bool = True,
        max_retries: int = 3,
    ) -> bool:
        """Download a YouTube video as MP4."""

        options = {
            **self.DEFAULT_OPTIONS,
            "format": f"bestvideo[height<={height}]+bestaudio/best[height<={height}]",
            "outtmpl": f"{dirpath}/{filename}.%(ext)s",
            "merge_output_format": "mp4",
            "noplaylist": noplaylist,
            "ignoreerrors": ignoreerrors,
        }

        outpath = Path(dirpath) / f"{filename}.mp4"
        return self._download(options=options, outpath=outpath, max_retries=max_retries)
