from typing import Literal

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QWidget
from searchresultsmodel import SearchResultModel
from ui_searchwidget import Ui_SearchWidget
from ytmusicapi import YTMusic

from yt_music.models.search_results import (
    AlbumSearchResult,
    SearchResult,
    SongSearchResult,
)


class SearchWidget(QWidget):
    item_selected = Signal(object)

    def __init__(self):
        super().__init__()
        self.ui = Ui_SearchWidget()
        self.ui.setupUi(self)

        self.yt = YTMusic()

        self.search_results_model = SearchResultModel(parent=self)
        self.ui.listResults.setModel(self.search_results_model)

        self.ui.radioAlbum.setChecked(True)
        self.search_filter: Literal["albums", "songs"] = "albums"

        self.ui.radioAlbum.clicked.connect(self.on_radio_toggled)
        self.ui.radioSong.clicked.connect(self.on_radio_toggled)
        self.ui.pushSearch.clicked.connect(self.handle_search_clicked)
        self.ui.pushSelect.clicked.connect(self.handle_select_clicked)

        self.ui.pushSelect.setEnabled(False)
        self.ui.listResults.selectionModel().currentChanged.connect(
            self.handle_selection_changed
        )
        self.ui.listResults.doubleClicked.connect(self.handle_select_clicked)

    def on_radio_toggled(self):
        if self.ui.radioAlbum.isChecked():
            self.search_filter = "albums"
        else:
            self.search_filter = "songs"

    def handle_search_clicked(self):
        query = self.ui.lineSearch.text().strip()
        if not query:
            return

        filter = self.search_filter

        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        try:
            results = self.yt.search(query=query, filter=filter)
        finally:
            QApplication.restoreOverrideCursor()

        search_results: list[SearchResult]
        match filter:
            case "albums":
                search_results = [AlbumSearchResult.model_validate(r) for r in results]
            case "songs":
                search_results = [SongSearchResult.model_validate(r) for r in results]

        self.search_results_model.set_search_results(search_results=search_results)

    def handle_selection_changed(self):
        self.ui.pushSelect.setEnabled(self.ui.listResults.currentIndex().isValid())

    def handle_select_clicked(self):
        current = self.search_results_model.search_result_at(
            self.ui.listResults.currentIndex()
        )
        if current is None:
            return

        self.item_selected.emit(current)
