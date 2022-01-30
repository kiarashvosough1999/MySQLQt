from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QListWidgetItem


class SQLButtonFactory:

    @staticmethod
    def sql_reserved_words() -> [str]:
        return [
            'CREATE',
            'Alter',
            'ORDER BY',
            'SELECT',
            'FROM',
            'WHERE',
            'INNER JOIN',
            'OUTER JOIN',
            'INSERT',
            'UPDATE',
            'DELETE',
            'CREATE',
            'TABLE',
            '*',
            'IN',
            'SOME',
            'AVG()',
            'COUNT()'
        ]

    @staticmethod
    def generate_reserved_words_list_items() -> [QListWidgetItem]:

        def mapper(text):
            list_item = QListWidgetItem(text)
            return list_item

        return list(map(mapper, SQLButtonFactory.sql_reserved_words()))




