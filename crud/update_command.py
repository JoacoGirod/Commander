import json
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.PersistenceManager import *
from models.Command import Command

def main():
    if len(sys.argv) != 3:
        print("Usage: update_command <command_name> <new_path>")
        return

    persistence_dao = PersistenceManager().get_implementation()

    # Add the new command to the command file
    if persistence_dao.update_command(sys.argv[1], sys.argv[2]):
        print("Command '" + sys.argv[1] + "' updated succesfully.")
    else:
        print(f"""Error: Command '{sys.argv[1]}' was not found.""")

if __name__ == "__main__":
    main()