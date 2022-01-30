from DBService.MYSQLService import MYSQLService
from Features.Dispalyer.QueryResultDisplayerView import QueryResultDisplayerView
from Features.Dispalyer.QueryResultDisplayerViewModel import QueryResultDisplayerViewModel
from Utils.Models.QueryResult import QueryResult
from Utils.SQLButtonFactory import SQLButtonFactory


class ExecuterViewModel:

    def __init__(self, db_service: MYSQLService):
        self.get_text_view_text = None
        self._db_service = db_service

    def execute_button_clicked(self):
        if self.get_text_view_text:
            self._get_execute_query(query=self.get_text_view_text())

    def _get_execute_query(self, query):
        model: QueryResult = self._db_service.fetch_all_as_2d_array(query)
        viewModel = QueryResultDisplayerViewModel(model=model)
        self.view = QueryResultDisplayerView(view_model=viewModel)
        self.view.resize(480, 320)
        self.view.show()


    @staticmethod
    def get_list_items():
        return SQLButtonFactory.generate_reserved_words_list_items()
