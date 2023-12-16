import os
import sqlite3
from utils import genera_bar_code
from constant import DB_NAME, QUERY_EAN_TO_UPDATE
from logger import logger


def update_ean():
    NAME_FILE = os.path.basename(__file__)
    logger_update = logger

    logger_update.info(
        f"{NAME_FILE} - Leggo dalla tabella gli ean da sovrascrivere .... -"
    )

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(QUERY_EAN_TO_UPDATE)
    logger_update.debug(f"{NAME_FILE} - Eseguo Query:  {QUERY_EAN_TO_UPDATE} -")

    righe_da_modificare = cursor.fetchall()
    cursor.close()
    conn.close()
    numero_righe = len(righe_da_modificare)

    logger_update.info(f"{NAME_FILE} - Genero {numero_righe} ean nuovi .... -")
    array_new_ean = []
    array_new_ean = genera_bar_code(numero_righe)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    indice = 0
    logger_update.info(
        f"{NAME_FILE} - Sovrascrivo {numero_righe} ean vecchi con i nuovi .... -"
    )
    tot_righe_to_commit = 1000
    for riga in righe_da_modificare[:numero_righe]:
        id, ean = riga

        update_query = (
            f"UPDATE prodotti SET ean ='{array_new_ean[indice]}' WHERE id ={id}"
        )
        cursor.execute(update_query)
        if indice % tot_righe_to_commit == 0:
            conn.commit()
            logger_update.debug(
                f"{NAME_FILE} - Eseguo un commit ogni {tot_righe_to_commit} update : indice riga:  {indice} -"
            )
        indice += 1

    conn.commit()
    logger_update.debug(f"{NAME_FILE} - Eseguo Commit a indice:  {indice} -")
    cursor.close()
    conn.close()
