from utils.logger import Logger
from data.config import LOGGER_LEVEL
logger = Logger()
logger.config(LOGGER_LEVEL, "Game of LIFE Import Checker")

def checkImport():
    try:
        import json
        import random
        import os
        logger.debug("All Imports Done")
    except:
        logger.error("Could not import ALL Dependencies")
