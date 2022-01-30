from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow
from Features.Executer.ExecuterViewModel import ExecuterViewModel
from Utils.Widgets.DragableQListWidget import DragableQListWidget
from Utils.Widgets.DropableQTextEdit import DropableQTextEdit


class ExecuterView(QMainWindow):

    def __init__(self, viewModel: ExecuterViewModel):
        super().__init__()

        self._viewModel = viewModel

        self.main_widget = QWidget()
        self.main_h_layout = QHBoxLayout()

        self.sql_commands_QListWidget_v_layout = QVBoxLayout()
        self.sql_commands_QListWidget = DragableQListWidget()

        self.right_side_v_layout = QVBoxLayout()

        self.configuration_v_layout = QHBoxLayout()

        self.text_edit = DropableQTextEdit()

        self.sql_buttons_h_layout = QHBoxLayout()

        self.execute_button = QPushButton("Execute")

        self.setupViews()
        self.setupBindings()

    def setupBindings(self):
        for item in ExecuterViewModel.get_list_items():
            self.sql_commands_QListWidget.addItem(item)

        self.execute_button.clicked.connect(self._viewModel.execute_button_clicked)

        self._viewModel.get_text_view_text = lambda: self.text_edit.toPlainText()

    def setupViews(self):
        self.sql_commands_QListWidget_v_layout.addWidget(self.sql_commands_QListWidget)

        self.sql_buttons_h_layout.addWidget(self.execute_button)

        self.configuration_v_layout.addWidget(self.text_edit)

        self.main_h_layout.addLayout(self.sql_commands_QListWidget_v_layout)

        self.right_side_v_layout.addLayout(self.configuration_v_layout)

        self.right_side_v_layout.addLayout(self.sql_buttons_h_layout)

        self.main_h_layout.addLayout(self.right_side_v_layout)

        self.main_widget.setLayout(self.main_h_layout)

        self.setCentralWidget(self.main_widget)
