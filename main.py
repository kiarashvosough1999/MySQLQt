import sys
from PyQt5.QtWidgets import QApplication
from DBService.MYSQLService import MYSQLService
from Features.NavigationView.NavigationView import NavigationView
from Features.NavigationView.NavigationViewModel import NavigationViewModel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog_1 = NavigationView(view_model=NavigationViewModel(db_service=MYSQLService()))
    dialog_1.show()
    dialog_1.resize(480, 320)
    sys.exit(app.exec_())
