from Utils.Models.QueryResult import QueryResult


class QueryResultDisplayerViewModel:

    def __init__(self, model: QueryResult):
        self._model = model

    def get_data(self):
        return self._model.data_array

    def get__row_count(self) -> int:
        return self._model.row_count

    def get__column_count(self) -> int:
        return self._model.column_count

    def get_horizontal_header_labels(self) -> [str]:
        return self._model.column_names

    def get_vertical_header_labels(self) -> [str]:
        return list(map(lambda number: str(number), [i for i in range(0, self.get__row_count())]))
