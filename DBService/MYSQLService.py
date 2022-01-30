import mysql
from mysql.connector import MySQLConnection

from Utils.Models.QueryResult import QueryResult


class MYSQLService:

    def __init__(self):
        self._mydb: MySQLConnection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pooya",
        )

    def execute_command(self, command):
        mycursor = self._mydb.cursor()
        return mycursor.execute(command)

    def fetch_all(self, command):
        mycursor = self._mydb.cursor()
        mycursor.execute(command)
        return mycursor.fetchall()

    def fetch_one(self, command):
        mycursor = self._mydb.cursor()
        mycursor.execute(command)
        return mycursor.fetchone()

    def fetch_all_as_2d_array(self, command):
        mycursor = self._mydb.cursor()
        mycursor.execute(command)
        all = mycursor.fetchall()

        return QueryResult(data_array=[[item for item in tuple] for tuple in all],
                           column_count=len(all[0] if all else 0),
                           row_count=len(all),
                           column_names=list(mycursor.column_names))
