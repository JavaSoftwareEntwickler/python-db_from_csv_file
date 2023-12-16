import os
import csv
import sqlite3
from logger import logger
from constant import DB_NAME, QUERY_ESISTE_IL_TABLE_PRODOTTI


def crea_tabella(nome_tabella, file_input):
    """
    Prende in input: il nome della tabella e il file csv
    Crea la tabella se non esiste con prima colonna PK e ne restituisce l'elenco
    delle colonne
    """
    NAME_FILE = os.path.basename(__file__)
    logger_ct = logger
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(QUERY_ESISTE_IL_TABLE_PRODOTTI)
    tabella_esiste = bool(cursor.fetchone())

    if tabella_esiste:
        logger_ct.info(f"{NAME_FILE} - Tabella già esistente ! -")
    else:
        logger_ct.info(f"{NAME_FILE} - Leggo la prima riga del csv {file_input} .... -")
        with open(file_input, "r", encoding="utf-8") as file:
            riga = csv.reader(file, delimiter=";")
            valori_colonne = next(riga)
            valori_colonne = [col.replace('"', "") for col in valori_colonne]
        primary_key_colonna = valori_colonne[0]

        create_table_query = f"CREATE TABLE IF NOT EXISTS {nome_tabella} ({primary_key_colonna} INTEGER PRIMARY KEY, {', '.join(valori_colonne[1:])});"
        cursor.execute(create_table_query)
        logger_ct.info(f"{NAME_FILE} - Creata la tabella .... :{nome_tabella} -")
    cursor.close()
    conn.close()
    return valori_colonne
