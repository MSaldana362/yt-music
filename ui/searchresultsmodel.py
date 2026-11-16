from PySide6.QtCore import QAbstractListModel, QModelIndex, QPersistentModelIndex, Qt

from yt_music.models.search_results import (
    AlbumSearchResult,
    SearchResult,
    SongSearchResult,
)


class SearchResultModel(QAbstractListModel):
    SearchResultRole = Qt.ItemDataRole.UserRole

    def __init__(self, search_results: list[SearchResult] | None = None, parent=None):
        super().__init__(parent)

        self._search_results: list[SearchResult] = list(search_results or [])

    def rowCount(
        self, parent: QModelIndex | QPersistentModelIndex | None = None
    ) -> int:
        if parent is not None and parent.isValid():
            return 0

        return len(self._search_results)

    def _display(self, search_result: SearchResult) -> str:
        if isinstance(search_result, AlbumSearchResult):
            return f"{search_result.artists_str} - {search_result.title} ({search_result.year})"
        if isinstance(search_result, SongSearchResult):
            return f"{search_result.artists_str} - {search_result.title}"

        return search_result.title

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):
        if not index.isValid() or not (0 <= index.row() < len(self._search_results)):
            return None

        search_result = self._search_results[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            return self._display(search_result)
        if role == self.SearchResultRole:
            return search_result

        return None

    def set_search_results(self, search_results: list[SearchResult]) -> None:
        self.beginResetModel()
        self._search_results = list(search_results)
        self.endResetModel()

    def search_result_at(self, index: QModelIndex) -> SearchResult | None:
        if not index.isValid() or not (0 <= index.row() < len(self._search_results)):
            return None
        return self._search_results[index.row()]
