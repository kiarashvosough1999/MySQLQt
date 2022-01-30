import typing

from PyQt5 import QtCore
from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import QAbstractItemView, QListWidget, QListWidgetItem


class DragableQListWidget(QListWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragOnly)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setAcceptDrops(True)

    def mimeData(self, items: typing.Iterable[QListWidgetItem]) -> QtCore.QMimeData:
        print("items: ", items)
        md = QMimeData()
        texts = []
        for item in self.selectedItems():
            texts.append(item.text())
        md.setText('\n'.join(texts))
        return md

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.IgnoreAction)
            event.accept()
        else:
            super().dragMoveEvent(event)
