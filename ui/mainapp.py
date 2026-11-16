"""Main Application"""

import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QMainWindow, QMessageBox
from searchdialog import SearchDialog
from ui_mainwindow import Ui_MainWindow

from yt_music.downloader import downloader
from yt_music.models.search_results import (
    AlbumSearchResult,
    SearchResult,
    SongSearchResult,
)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("YouTube MP3 Downloader")
        self.resize(800, 400)

        self.pushSearch.clicked.connect(self.handle_search_clicked)
        self.pushDownload.clicked.connect(self.handle_download_clicked)
        self.pushOpenUrl.clicked.connect(self.handle_open_url_clicked)
        self.pushClear.clicked.connect(self.handle_clear_clicked)

    def handle_search_clicked(self) -> None:
        dialog = SearchDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            selected_item = dialog.selected_item
            if selected_item is not None:
                self.handle_search_result(search_result=selected_item)

    def _set_text(self, line_edit: QLineEdit, value: str | None) -> None:
        """Set text for a QLineEdit if valid."""
        if value:
            line_edit.setText(value)

    def handle_search_result(self, search_result: SearchResult) -> None:
        if isinstance(search_result, AlbumSearchResult):
            self._set_text(self.lineUrl, search_result.playlist_url)
            self._set_text(self.lineArtist, search_result.artists_str)
            self._set_text(self.lineAlbum, search_result.title)
            self._set_text(self.lineYear, search_result.year)
            self._set_text(self.lineArt, search_result.artwork_url)
        if isinstance(search_result, SongSearchResult):
            self._set_text(self.lineUrl, search_result.song_url)
            self._set_text(self.lineArtist, search_result.artists_str)
            self._set_text(self.lineAlbum, search_result.album_str)
            self._set_text(self.lineYear, search_result.year)

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

    def handle_open_url_clicked(self):
        if self.lineUrl.text():
            url = QUrl(self.lineUrl.text())
            QDesktopServices.openUrl(url)

    def handle_clear_clicked(self):
        for line_edit in self.findChildren(QLineEdit):
            line_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
