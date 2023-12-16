import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename=f"logger_db.log",
    filemode="a",
    format=Log_Format,
    level=logging.NOTSET,
)
logger = logging.getLogger(__name__)
