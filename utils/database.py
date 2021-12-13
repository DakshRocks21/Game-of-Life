from utils.logger import Logger
import json

from data.config import LOGGER_LEVEL
logger = Logger()
logger.config(LOGGER_LEVEL, "Game of LIFE database")

def addData():
    logger.debug("Creating Data File")
    try:
        with open("data/example.json", "r") as f:
            example_data = json.load(f)
        with open("data/data.json", "w") as f:
            json.dump(example_data, f, indent=4)
    except:
        logger.critical("Could not add data to the data file")


def createDataFile():
    try:
        open("data/data.json", 'a').close()
        logger.debug("data file created successfully")
    except:
        logger.critical("Could not create the data file")


def setup():
    createDataFile()
    addData()

