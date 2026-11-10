"""
YouTube Downloader to MP3
"""

import argparse
import logging
from pathlib import Path

from yt_music.classes.image_file import ImageFile
from yt_music.classes.mp3_file import Mp3File, Mp3Tags
from yt_music.classes.music_utils import AlbumUtils, SingleUtils
from yt_music.classes.youtube_url import YouTubeUrl

logging.basicConfig(level=logging.INFO)


def downloader(
    url: str,
    artist: str,
    album: str,
    year: int,
    art: str | None = None,
    genre: str | None = None,
) -> None:
    """Download to MP3"""

    youtube_url = YouTubeUrl(url)
    youtube_url.get_info()

    playlist_urls = youtube_url.playlist_urls()

    if playlist_urls:

        # create album directory and info file

        dirpath = AlbumUtils.create_album_dir(artist, album, year)

        AlbumUtils.create_info_txt(
            dirpath=dirpath, url=youtube_url.url, titles=youtube_url.playlist_titles()
        )

        # download album artwork

        artpath = None
        if art is not None:
            image = ImageFile(url=art)
            artpath = image.download(dirpath=dirpath, filename=f"_{album}")

        # download playlist entries, apply metadata, and rename

        for index, entry in enumerate(playlist_urls, start=1):
            entry_url = YouTubeUrl(entry)
            entry_url.get_info()

            title = entry_url.title()

            filename = title
            filepath = dirpath / f"{filename}.mp3"

            entry_url.download_to_mp3(dirpath, filename)

            mp3 = Mp3File(Path(filepath))
            mp3.set_tags(
                tags=Mp3Tags(
                    artist=artist,
                    album=album,
                    year=year,
                    track_name=title,
                    track_number=index,
                    genre=genre,
                )
            )

            if artpath is not None:
                mp3.apply_album_art(artpath=artpath)

            mp3.rename_for_album()

    else:

        # create artist directory

        dirpath = SingleUtils.create_artist_dir(artist=artist)

        # download album artwork

        artpath = None
        if art is not None:
            image = ImageFile(url=art)
            artpath = image.download(dirpath=dirpath, filename=f"_{album}")

        # download, apply metadata, and rename

        title = youtube_url.title()

        filename = title
        filepath = dirpath / f"{filename}.mp3"

        youtube_url.download_to_mp3(dirpath=dirpath, filename=filename)

        mp3 = Mp3File(Path(filepath))
        mp3.set_tags(
            tags=Mp3Tags(
                artist=artist,
                album=album,
                year=year,
                track_name=title,
                genre=genre,
            )
        )

        if artpath is not None:
            mp3.apply_album_art(artpath=artpath)

        mp3.rename_for_single()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Download a playlist or video from YouTube as MP3.",
        usage="python downloader.py --help",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("url", type=str, help="URL of YouTube playlist or video")
    parser.add_argument("artist", type=str, help="Artist")
    parser.add_argument("album", type=str, help="Album")
    parser.add_argument("year", type=int, help="Year")
    parser.add_argument("--art", type=str, help="URL of album art")
    parser.add_argument("--genre", type=str, help="Genre")

    args = parser.parse_args()

    downloader(
        url=args.url,
        artist=args.artist,
        album=args.album,
        year=args.year,
        art=args.art,
        genre=args.genre,
    )

# "https://music.youtube.com/watch?v=D-6FeedpTpg" "Rex Orange County" "Sunflower" 2017 --art "https://yt3.googleusercontent.com/aFvGyJ4Mgv9j7_L-UCxtMWd71ph6R-dseRKCb4TaUf3RE6vpUwzIcZ8YHD6ybphXTcbotdr8JauIkfHK=w544-h544-l90-rj"

# "https://music.youtube.com/playlist?list=OLAK5uy_nXCZ714FRe9Gr96c9Ycuqummnv8W-dfEs" "The Serpent (In Quicksilver)" "Harold Budd" 1981 --art "https://yt3.googleusercontent.com/IA5kmKcp8gXxbsBJHefaTKg6utBuhiBE0xN8kdyzz5hvz0q5-eplc1VpADhYTf2ZYWZ4swgDtLIk9WVb=w544-h544-l90-rj" --genre "Ambient"
