# YouTube Music Download MP3

A command line tool to download music from YouTube.

Download a single video or a playlist and apply the music tags in one command, with the option to download and apply album art as well. Utilizes [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) and [`eyed3`](https://eyed3.readthedocs.io/en/v0.9.8/).

It is recommended to use [YouTube Music](https://music.youtube.com/) for finding music albums.

## Usage

```
python download_mp3.py [YOUTUBE_URL] [ARTIST] [ALBUM] [YEAR][--artwork-url ARTWORK_URL]

Download a playlist or video from YouTube as a music album or single.

positional arguments:
  youtube_url           URL of the YouTube playlist or video.
  artist                The artist name of the album or single.
  album                 The album or single title.
  year                  The year of the album or single.

options:
  -h, --help            show this help message and exit
  --artwork-url ARTWORK_URL
                        URL of the album artwork. (default: None)
```

## Example

Let's say I wanted to download the album [Shinkeisuijyaku (1981) by Tomoko Aran](https://music.youtube.com/playlist?list=OLAK5uy_kAGXrLmhZUFjJV7mFVuuRh6wuUADku5Nc&si=ohD71vxs1iJCM84A) from YouTube Music. To download the album without the album artwork, I would run the following command:

```
poetry run python /yt-music-download/download_mp3.py "https://music.youtube.com/playlist?list=OLAK5uy_kAGXrLmhZUFjJV7mFVuuRh6wuUADku5Nc&feature=shared" "Tomoko Aran" " Shinkeisuijyaku" 1981
```

YouTube Music has the album artwork, so I can right-click on the image and copy the image link. So if I want to download the album tracks with the artwork applied, I can add this link to the `--artwork-url` option:

```
poetry run python /yt-music-download/download_mp3.py "https://music.youtube.com/playlist?list=OLAK5uy_kAGXrLmhZUFjJV7mFVuuRh6wuUADku5Nc&feature=shared" "Tomoko Aran" " Shinkeisuijyaku" 1981 --artwork-url "https://lh3.googleusercontent.com/Rfze1ipyLQihWaEK7KqdCy_JFE37JgUxWpgWUYeEwnLWJzSVN_slsB4hA4lbDVbasDma71rdanPrsjTe=w544-h544-s-l90-rj"
```
