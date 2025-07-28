"""
Main application.
"""

import sys
from PyQt5 import QtWidgets
from ui.download_mp3_ui import Ui_MainWindow
from download_mp3 import download_mp3


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonDownload.clicked.connect(self.download)

    def download(self):
        """
        Download video or playlist to MP3.
        """

        youtube_url = self.ui.lineEditUrl.text()
        if not youtube_url:
            print("Please enter a valid YouTube url.")
            return

        artist = self.ui.lineEditArtist.text()
        if not artist:
            print("Please enter a valid artist name.")
            return

        album = self.ui.lineEditAlbum.text()
        if not album:
            print("Please enter a valid album name.")
            return

        try:
            year = int(self.ui.lineEditYear.text())
        except ValueError:
            print("Please enter a valid year.")
            return

        artwork_url = self.ui.lineEditArtwork.text()
        if not artwork_url:
            artwork_url = None

        try:
            download_mp3(
                youtube_url=youtube_url,
                artist=artist,
                album=album,
                year=year,
                artwork_url=artwork_url,
            )
            print("Download compleeted successfully. You may now close the window.")
        except RuntimeError:
            print("Something went wrong when trying to download from YouTube.")
            return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
