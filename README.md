# YouTube Music: Download to MP3

A simple tool to download music from [YouTube Music](https://music.youtube.com/) to MP3 using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) and apply MP3 tags using [`eyed3`](https://eyed3.readthedocs.io/en/v0.9.8/).

Also utilizes [`ytmusicapi`](https://ytmusicapi.readthedocs.io/en/stable/) to help search for music from YouTube Music.

## Prerequisites

The computer running the application must have [`ffmpeg`](https://ffmpeg.org/) installed.

For development, install the following:
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Qt Creator](https://www.qt.io/development/download-qt-installer-oss)

Once the repository has been cloned and `uv` has been installed, run the command:

```
uv sync
```

This will create the Python virtual environment according to the `pyproject.toml` and `uv.lock` files.

## Usage

Provide the URL to a YouTube Music album or song, as well as the following metadata:
- Artist
- Album
- Year
- Artwork URL (Optional)
- Genre (Optional)

The tool will download each song individually. After each download, the provided metadata will be applied to the MP3 file.

The YouTube Music API can be used to search YouTube Music for an album or song. Select the item from the search results, and if metadata is found it will be applied automatically.

## Development

The GUI application is built using Qt for Python ([`pyside6`](https://pypi.org/project/PySide6/)).

### Qt Creator UI Files

All Qt `.ui` files are created using Qt Creator and must be converted to `.py` files. The `pyside6-uic` tool is used to perform this conversion using the following command:

```
uv run pyside6-uic ./ui/mainwindow.ui -o ./ui/ui_mainwindow.py
```

### Builds

This project uses `pyinstaller` to create builds of the application. Run the following command:

```
uv run pyinstaller --noconsole --onefile --collect-data ytmusicapi  ./ui/mainapp.py
```

Note the inclusion of `--collect-data ytmusicapi`, which is required in order for the built application to run successfully.