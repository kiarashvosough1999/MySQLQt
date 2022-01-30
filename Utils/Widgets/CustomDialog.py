from PyQt5.QtWidgets import QDialogButtonBox, QVBoxLayout, QLabel, QDialog


class CustomDialog(QDialog):

    def __init__(self, message: str, title: str):
        super().__init__()

        self.setWindowTitle(title)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(message)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)