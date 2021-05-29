from requests import get
def main(args):

    logger = setupLogger(args.debug)

    userName = args.userName
    url = f"https://api.chess.com/pub/player/{userName}" 

    logger.debug(f"Using url {url}")

    logger.info("Retrieving info")
    r = get(url)
    print(r.status_code)

    logger.debug(r.json())

#====================================================================================================

def setupLogger(doDebug):
    """ setup logger """

    import logging

    level = logging.INFO if not doDebug else logging.DEBUG

    logging.basicConfig()
    logging.root.setLevel(level)
    logging.basicConfig(level = level)

    logger  = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setLevel(level)

    formatter = logging.Formatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

#====================================================================================================

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--userName", metavar = "USERNAME", type = str, help = "chess.com username", required = False, default = "sddish")
    parser.add_argument("--debug", action = "store_true")

    args = parser.parse_args()
    main(args)
