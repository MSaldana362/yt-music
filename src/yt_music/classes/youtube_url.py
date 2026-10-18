from pathlib import Path
from typing import Any
import yt_dlp


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

    def download_to_mp3(
        self,
        dirpath: str,
        filename: str,
        noplaylist: bool = False,
        ignoreerrors: bool = True,
    ) -> bool:
        """
        Download a YouTube video as MP3.

        Args:
            dirpath (str): _description_
            filename (str): _description_
            noplaylist (bool, optional): _description_. Defaults to False.
            ignoreerrors (bool, optional): _description_. Defaults to True.
        """

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

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([self.url])

        outpath = Path(dirpath) / f"{filename}.mp3"
        return outpath.exists()

    def download_to_mp4(
        self,
        dirpath: str,
        filename: str,
        height: int,
        noplaylist: bool = False,
        ignoreerrors: bool = True,
    ) -> bool:
        """
        Download a YouTube video as MP4.

        Args:
            dirpath (str): _description_
            filename (str): _description_
            height (int): _description_
            noplaylist (bool, optional): _description_. Defaults to False.
            ignoreerrors (bool, optional): _description_. Defaults to True.
        """

        options = {
            **self.DEFAULT_OPTIONS,
            "format": f"bestvideo[height<={height}]+bestaudio/best[height<={height}]",
            "outtmpl": f"{dirpath}/{filename}.%(ext)s",
            "merge_output_format": "mp4",
            "noplaylist": noplaylist,
            "ignoreerrors": ignoreerrors,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([self.url])

        outpath = Path(dirpath) / f"{filename}.mp4"
        return outpath.exists()
