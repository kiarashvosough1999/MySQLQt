from PyQt5.QtWidgets import QStackedWidget
from Features.Executer.ExecuterView import ExecuterView
from Features.Executer.ExecuterViewModel import ExecuterViewModel
from Features.Login.LoginView import LoginView
from Features.Login.LoginViewModel import LoginViewModel
from Features.NavigationView.NavigationViewModel import NavigationViewModel


class NavigationView(QStackedWidget):

    def __init__(self, view_model: NavigationViewModel):
        super().__init__()
        self._view_model = view_model

        executer_viewmodel = ExecuterViewModel(db_service=self._view_model.get_db_service())
        login_view_model = LoginViewModel(db_service=self._view_model.get_db_service(),
                                          user_logged_in=self._change_index)

        self.addWidget(LoginView(view_model=login_view_model))
        self.addWidget(ExecuterView(viewModel= executer_viewmodel))

    def _change_index(self):
        self.setCurrentIndex(1 if self.currentIndex() == 0 else 0)
