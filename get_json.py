from requests import get
from utils.string_utils import INFO, DEBUG

def main(args):

    userName = args.userName
    url = f"https://api.chess.com/pub/player/{userName}" 

    args.debug and DEBUG(f"Using url {url}")

    r = get(url)

    args.debug and print(r.json())

#====================================================================================================

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--userName", metavar = "USERNAME", type = str, help = "chess.com username", required = False, default = "sddish")
    parser.add_argument("--debug", action = "store_true")

    args = parser.parse_args()
    main(args)
