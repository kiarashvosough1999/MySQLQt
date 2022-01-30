
class QueryResult:

    def __init__(self, data_array,
                 column_count: int,
                 row_count: int,
                 column_names: [str]):
        self.data_array = data_array
        self.column_count = column_count
        self.row_count = row_count
        self.column_names = column_names