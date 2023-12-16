import os
import csv
import sqlite3
from logger import logger
from constant import DB_NAME, PRODOTTI_FILE_CSV_INPUT


def carica_tabella(tabella, column_names):
    NAME_FILE = os.path.basename(__file__)
    logger_insert = logger

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    with open(PRODOTTI_FILE_CSV_INPUT, "r", encoding="utf-8") as file:
        logger_insert.info(
            f"{NAME_FILE} - Leggo i dati dal csv e li inserisco nella tabella .... - {tabella}"
        )

        righe = csv.DictReader(file, delimiter=";")
        for riga in righe:
            valori = [riga[col] for col in column_names]
            insert_query = f"INSERT INTO {tabella} VALUES ({', '.join(['?' for _ in range(len(column_names))])});"
            cursor.execute(insert_query, valori)
    conn.commit()
    cursor.close()
    conn.close()
