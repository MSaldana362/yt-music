"""Album Utils"""

from pathlib import Path


class AlbumUtils:
    """Utility class with static helper methods."""

    def __init__(self):
        raise TypeError("Utility class, cannot instantiate.")

    @staticmethod
    def create_info_txt(dirpath: str | Path, url: str, titles: list[str]) -> None:
        """Create info TXT file."""

        dirpath = Path(dirpath)
        filepath = dirpath / "_info.txt"

        lines = [dirpath.name, url, ""]

        for index, title in enumerate(titles, start=1):
            lines.append("\t".join([f"{index:02d}", title]))

        filepath.write_text("\n".join(lines) + "\n", encoding="utf-8")
