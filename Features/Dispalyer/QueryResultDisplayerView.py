from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from Features.Dispalyer.QueryResultDisplayerViewModel import QueryResultDisplayerViewModel


class QueryResultDisplayerView(QTableWidget):

    def __init__(self, view_model: QueryResultDisplayerViewModel):
        super().__init__()

        self._view_model = view_model
        self.setRowCount(self._view_model.get__row_count())
        self.setColumnCount(self._view_model.get__column_count())
        self.setHorizontalHeaderLabels(self._view_model.get_horizontal_header_labels())
        self.setVerticalHeaderLabels(self._view_model.get_vertical_header_labels())

        for i in range(0,self._view_model.get__row_count()):
            for j in range(0, self._view_model.get__column_count()):
                self.setItem(i, j, QTableWidgetItem(str(self._view_model.get_data()[i][j])))

        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
