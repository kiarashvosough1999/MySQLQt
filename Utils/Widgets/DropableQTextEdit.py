from PyQt5.QtGui import QDropEvent
from PyQt5.QtWidgets import QTextEdit
from PyQt5 import QtCore


class DropableQTextEdit(QTextEdit):
    dropped = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        mime = event.mimeData()
        if mime.hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasText():
            # event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            self.setText(self.toPlainText() + " " + event.mimeData().text())

            # self.emit(self.dropped, links)
        else:
            event.setDropAction(QtCore.Qt.TargetMoveAction)
            super().dropEvent(event)
