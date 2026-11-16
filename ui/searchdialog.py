from PySide6.QtWidgets import QDialog, QFormLayout
from searchwidget import SearchWidget

from yt_music.models.search_results import SearchResult


class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Search for Music")
        self.resize(600,300)

        self.widget = SearchWidget()
        layout = QFormLayout(self)
        layout.addWidget(self.widget)

        self.selected_item: SearchResult | None = None

        self.widget.item_selected.connect(self.on_item_selected)

    def on_item_selected(self, search_result: SearchResult):
        self.selected_item = search_result
        self.accept()
