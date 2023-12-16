import os
from logger import logger
from update_bar_code import update_ean
from crea_tabella_prodotti import crea_tabella
from carica_prodotti import carica_tabella
from constant import scrivi_time_stamp, PRODOTTI_FILE_CSV_INPUT

NAME_FILE = os.path.basename(__file__)
logger_main = logger

logger_main.info(f"{NAME_FILE} - Start :")
scrivi_time_stamp()

nomi_colonne_tabella = crea_tabella("prodotti", PRODOTTI_FILE_CSV_INPUT)
carica_tabella("prodotti", nomi_colonne_tabella)
update_ean()

logger_main.info(f"{NAME_FILE} - Fine: -")
scrivi_time_stamp()
