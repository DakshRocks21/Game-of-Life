import random
from utils.logger import Logger
import json

from data.config import LOGGER_LEVEL
logger = Logger()
logger.config(LOGGER_LEVEL, "Game of LIFE database")


def addData(player_count):
    with open("data/example.json", "r") as f:
        example_data = json.load(f)

    logger.debug(f"Trying to create {player_count} profiles")

    file_data = json.load(open("data/data.json"))

    player_data = []

    for i in range(player_count):
        path_input = str(input(f"\nPlayer {i+1}: Choose a Path\n1. College\n2. Career\n>>> "))
        if path_input == "1":
            path_option = "College"
        else:
            path_option = "Career"

        print(f"Player {i+1} choose {path_option}")
        logger.debug(f"Player {i+1} choose {path_option}")

        temp_data = example_data
        temp_data["path"] = path_option
        print(temp_data)
        print("")
        print("")
        print(player_data)
        player_data.append(temp_data)
        print(player_data)
        logger.critical("The Second Append overwrites First's Append")
        logger.debug(f"Added Player {i+1}'s data")
    
    logger.debug(f" Length of player_data: {len(player_data)}, Number of Players: {player_count}")
    logger.debug(f"Attempting Dump of data")
    try:
        with open("data/data.json", "w") as f:
            json.dump(player_data, f, indent=4)
        logger.debug(f"Dump of data DONE")
    except:
        logger.critical("Could not add player_data to the data file")


def setup():
    logger.debug("Creating Data File")
    try:
        with open("data/data.json", "w") as f:
            f.write("[]")
            f.close()
        logger.debug("data file created successfully")
    except:
        logger.critical("Could not create the data file")


def setPath(path_option):
    if path_option == "1":
        path_option = "College"
    else:
        path_option = "Career"
    data = json.load(("data.json").read)
    data["path"] = path_option
    with open("data/data.json", "w") as f:
        json.dump(data, f, indent=4)


def spin():
    value = random.randint(1, 10)
    return value
