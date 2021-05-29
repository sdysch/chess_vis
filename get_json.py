from requests import get
import logging

def main(args):

    setupLogger(args.debug)

    userName = args.userName
    url = f"https://api.chess.com/pub/player/{userName}" 

    logging.debug(f"Using url {url}")

    logging.info("Retrieving info")
    r = get(url)

    logging.debug(r.json())

#====================================================================================================

def setupLogger(doDebug):
    level = logging.INFO if not args.debug else logging.DEBUG
    logging.basicConfig(level = level, format = "%(levelname)s: %(message)s")

#====================================================================================================

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--userName", metavar = "USERNAME", type = str, help = "chess.com username", required = False, default = "sddish")
    parser.add_argument("--debug", action = "store_true")

    args = parser.parse_args()
    main(args)
