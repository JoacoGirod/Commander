import sys
import os

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from persistence.PersistenceManager import *
from models.Command import Command

def main():
    if len(sys.argv) != 2:
        print("Usage: delete_command <command_name>")
        return

    # Delete bash script
    try:
        os.remove(f"/usr/local/bin/{sys.argv[1]}")
    except PermissionError:
        print("This command requires sudo privileges.")
        return
    except FileNotFoundError:
        print(f"Error: Command '{sys.argv[1]}' was not found.")
        return

    # Delete command from the command file
    try:
        PersistenceManager().get_implementation().delete_command(sys.argv[1])
    except FileNotFoundError:
        print(f"Error: Command '{sys.argv[1]}' was not found.")
        return



    print(f"Command '{sys.argv[1]}' succesfully deleted.")

if __name__ == "__main__":
    main()