import requests
import logging
from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint

#====================================================================================================

# create module logger
module_logger = logging.getLogger(__name__)

#====================================================================================================

class DataStore:
    """ Core class to store data for a single chess.com user """

    def __init__(self, userName):
        self.userName = userName

        # setup logger
        self.setupLogger()

        # pretty printing
        self.printer = pprint.PrettyPrinter()

        self.logger.debug(f"Setup logger for chess.com user {self.userName}")

    #====================================================================================================

    def setupLogger(self):
        """ setup logger """

        # top logging level
        level = logging.INFO

        # setup basic logging
        logging.basicConfig(level = level)

        # configure stream handler
        formatter = logging.Formatter("%(levelname)s: %(message)s")

        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(level)
        streamHandler.setFormatter(formatter)

        # add stream handler to logger
        self.logger = logging.getLogger(__name__ + ".DataStore")
        self.logger.addHandler(streamHandler)

#====================================================================================================
