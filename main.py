from utils.logger import Logger

from data.config import LOGGER_LEVEL
logger = Logger()
logger.config(LOGGER_LEVEL, "Game of LIFE MAIN")

logger.info("Starting GAME")
logger.debug("Trying to Import Dependencies")

try:
    import json
    from utils import database 
    import random
    logger.debug("All Imports Done")
except:
    logger.error("Could not import ALL Dependencies")

database.setup()
logger.info("Set-up Complete")

