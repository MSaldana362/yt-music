"""Main Application"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_mainwindow import Ui_MainWindow
from yt_music.downloader import downloader


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("YouTube MP3 Downloader")
        self.resize(600, 400)

        self.pushDownload.clicked.connect(self.handle_download_clicked)

    def _validate_required(self) -> bool:
        """Ensure non-empty fields for required."""

        if not self.lineUrl.text():
            return False
        if not self.lineArtist.text():
            return False
        if not self.lineAlbum.text():
            return False
        if not self.lineYear.text():
            return False

        return True

    def handle_download_clicked(self):
        """Downloader"""

        if self._validate_required():
            try:
                downloader(
                    url=self.lineUrl.text().strip(),
                    artist=self.lineArtist.text().strip(),
                    album=self.lineAlbum.text().strip(),
                    year=int(self.lineYear.text().strip()),
                    art=self.lineArt.text().strip() or None,
                    genre=self.lineGenre.text().strip() or None,
                )
                QMessageBox.information(
                    self, "Completed", "Download completed successfully."
                )
            except Exception:
                QMessageBox.warning(
                    self, "Error", "Something went wrong. Please try again."
                )
        else:
            QMessageBox.information(
                self, "Missing Information", "Please enter required information."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
