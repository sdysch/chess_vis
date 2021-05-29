from requests import get
import logging

def main(args):

    setupLogger(args.debug)

    userName = args.userName
    url = f"https://api.chess.com/pub/player/{userName}" 

    logging.debug(f"Using url {url}")

    logging.info("Retrieving info...")
    r = get(url)

    # did we get the data OK?
    OK = handleResponse(r.status_code)
    if not OK:
        exit(1)

    logging.debug(r.json())

#====================================================================================================

def handleResponse(status_code):
    # ref: https://www.chess.com/news/view/published-data-api
    if status_code != 200:
        logging.critical("Could not obtain data")
        return False
    return True

#====================================================================================================

def setupLogger(doDebug):
    """ setup logger """

    level = logging.INFO if not doDebug else logging.DEBUG
    logging.basicConfig(level = level, format = "%(levelname)s: %(message)s")

#====================================================================================================

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--userName", metavar = "USERNAME", type = str, help = "chess.com username", required = False, default = "sddish")
    parser.add_argument("--debug", action = "store_true")

    args = parser.parse_args()
    main(args)
