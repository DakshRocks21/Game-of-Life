from utils.logger import Logger
from data.config import LOGGER_LEVEL

logger = Logger()
logger.config(LOGGER_LEVEL, "Game of LIFE MAIN")

logger.info("Starting GAME")
logger.debug("Trying to Import Dependencies")


from utils import database, check_imports

check_imports.checkImport()
database.setup()
logger.info("Set-up Complete")

try:
    players_input = int(input("How many people are playing? : "))
except ValueError:
    print("Please enter a Number")
    logger.critical("A number was not given for 'How many people are playing?' ")

if players_input <= 0:
    logger.info("0 people playing")
else:
    logger.info(f"{players_input} people playing")

database.addData(players_input)
2