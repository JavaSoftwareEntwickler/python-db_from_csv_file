import sqlite3
from sqlite3 import Error
from constant import DB_NAME


class BarCodeDaSovrascrivere:
    def __init__(self):
        self.bar_code_da_sostituire = 0
        self.conn = self.create_connection(DB_NAME)
        with self.conn:
            self.bar_code_da_sostituire = self.select_ean_null_or_less_then_13_char()
            self.conn.close

    def get_num_bar_code(self):
        return self.bar_code_da_sostituire

    def create_connection(self, db_file):
        """create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def select_all_tasks(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM prodotti")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def select_ean_null_or_less_then_13_char(self):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("SELECT ean FROM prodotti WHERE length(EAN) < 13 or EAN = ''")

        rows = cur.fetchall()
        return len(rows)
