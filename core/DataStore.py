import requests
import logging
from chessdotcom import get_player_stats, get_player_game_archives
import pprint

#====================================================================================================

class DataStore:
    """ Core class to store data for a single chess.com user """

    def __init__(self, userName):
        self.userName = userName

        # setup logger
        self.setupLogger()

        # pretty printing
        self.printer = pprint.PrettyPrinter()

        self.logger.debug(f"Setup chess.com user {self.userName}")

    #====================================================================================================

    def setupLogger(self):
        """ setup logger """

        level = logging.INFO
        logging.basicConfig(level = level, format = "%(levelname)s: %(message)s")
        self.logger = logging.getLogger(__name__)

    #====================================================================================================

    def getCurrentPlayerRatings(self):
        """ Get this player's current chess.com ratings """

        self.logger.info(f"Obtaining current ratings for {self.userName}")

        data = get_player_stats(self.userName).json["stats"]
        categories = ["chess_blitz", "chess_rapid", "chess_bullet", "chess_daily"]

        # get and store all ratings
        self.playerRatings = {}
        for category in categories:
            rating = data[category]["last"]["rating"]
            self.playerRatings[category] = rating

            self.logger.debug(f"{category} rating: {rating}")

    #====================================================================================================

    def printCurrentPlayerRatings(self):
        """ Print this player's current chess.com ratings """

        if not hasattr(self, "playerRatings"):
            self.logger.debug("Current player ratings not known, obtaining now....")
            self.getCurrentPlayerRatings()

        self.printer.pprint(self.playerRatings)
