import sys
import os
from datetime import datetime

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.Command import Command
from models.enums.FilePermission import *
from persistence.PersistenceManager import *

def main():
    if len(sys.argv) != 1:
        print("Usage: erase_all_commands")
        return

    if input("This command will delete all the bash files that were created and the persistence strategy, are you sure? Y/n\n") != "Y":
        return


    PersistenceManager().get_implementation().reset_implementation()
    ConfigurationManager().delete_configuration()

    print("Erasure was succesful.")

if __name__ == "__main__":
    main()
