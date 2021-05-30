from core import DataStore

def main(args):

    # setup data store
    store = DataStore.DataStore(args.userName)
    store.getCurrentPlayerRatings()
    store.printCurrentPlayerRatings()


#====================================================================================================

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--userName", metavar = "USERNAME", type = str, help = "chess.com username", required = False, default = "sddish")
    #parser.add_argument("--debug", action = "store_true") # FIXME to implement

    args = parser.parse_args()
    main(args)
