from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QSpacerItem, QSizePolicy
from Features.Login.LoginViewModel import LoginViewModel


class LoginView(QWidget):

    def __init__(self, view_model: LoginViewModel):
        super().__init__()
        self._view_model = view_model
        self._main_v_layout = QVBoxLayout()

        self._user_name_h_layout = QHBoxLayout()
        self._user_name_label = QLabel("Username")
        self._user_name_text_edit = QTextEdit()

        self._password_h_layout = QHBoxLayout()
        self._password_label = QLabel("Username")
        self._password_text_edit = QTextEdit()

        self._login_button = QPushButton("Login")

        self._setup_widgets()

    def _setup_widgets(self):
        self._view_model.get_password = lambda: self._password_text_edit.toPlainText()
        self._view_model.get_user_email = lambda: self._user_name_text_edit.toPlainText()

        self._login_button.clicked.connect(self._view_model.login_button_clicked)

        self._user_name_h_layout.addWidget(self._user_name_label)
        self._user_name_h_layout.addWidget(self._user_name_text_edit)

        self._password_h_layout.addWidget(self._password_label)
        self._password_h_layout.addWidget(self._password_text_edit)

        self._main_v_layout.addLayout(self._user_name_h_layout)

        space_1 = QSpacerItem(10, 90, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self._main_v_layout.addItem(space_1)

        self._main_v_layout.addLayout(self._password_h_layout)

        space_2 = QSpacerItem(10, 90, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self._main_v_layout.addItem(space_2)

        self._main_v_layout.addWidget(self._login_button)

        self.setLayout(self._main_v_layout)
