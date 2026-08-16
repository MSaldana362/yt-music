import argparse
import json
import yt_dlp


def print_as_json(info: dict):
    json_str = json.dumps(info, indent=4)
    print(json_str)


def get_track_info(url: str):
    options = {"extract_flat": True, "playlistend": None}
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            info = ydl.extract_info(url, download=False)

            # title = info["title"]
            # print(f"TITLE: {title}")

            album = info["album"]
            release_year = info["release_year"]
            print(f"\tALBUM: {album} ({release_year})")

            artists = info["artists"]
            print("\tARTISTS:")
            for artist in artists:
                print(f"\t\t{artist}")

        except Exception as e:
            raise RuntimeError(f"Error: Failed to extract info. {e}") from e


def get_album_info(url: str):

    options = {"extract_flat": True, "playlistend": None}
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            info = ydl.extract_info(url, download=False)

            print("THUMBNAILS".center(50, "-"))
            thumbnails = info["thumbnails"]
            for thumbnail in thumbnails:
                print(f"({thumbnail["resolution"]}): {thumbnail["url"]}")

            # print("TRACKS".center(50, "-"))
            # entries = info["entries"]
            # for entry in entries:
            #     get_track_info(entry["url"])

            get_track_info(info["entries"][0]["url"])

        except Exception as e:
            raise RuntimeError(f"Error: Failed to extract info. {e}") from e


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get YouTube Music information for an album.",
        usage="python -m tools.get_album_info [URL]",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("url", type=str, help="YouTube Music album URL.")

    args = parser.parse_args()

    get_album_info(url=args.url)
