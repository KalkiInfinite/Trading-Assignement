import logging
import os

def get_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("logs/bot.log")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(fh)
    return logger