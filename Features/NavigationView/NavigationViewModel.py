from DBService.MYSQLService import MYSQLService
from Features.Executer.ExecuterView import ExecuterView
from Features.Executer.ExecuterViewModel import ExecuterViewModel
from Features.Login.LoginViewModel import LoginViewModel


class NavigationViewModel:

    def __init__(self, db_service: MYSQLService):
        self._db_service = db_service

    def get_db_service(self):
        return self._db_service