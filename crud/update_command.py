import sys
import os

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from persistence.PersistenceManager import *
from models.Command import Command

def main():
    if len(sys.argv) != 3:
        print("Usage: update_command <command_name> <new_path>")
        return

    # Handle possible results of update_command
    try:
        if PersistenceManager().get_implementation().update_command(sys.argv[1], sys.argv[2]):
            print("Command '" + sys.argv[1] + "' updated succesfully.")
        else:
            print(f"""Error: Command '{sys.argv[1]}' was not found.""")
    except PermissionError:
        print("This command requires sudo privileges.")
        return
    except FileNotFoundError:
        print(f"""Error: Command '{sys.argv[1]}' was not found.""")
        return

if __name__ == "__main__":
    main()