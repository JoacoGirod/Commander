import json
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.PersistenceManager import *
from models.Command import Command

def main():
    if len(sys.argv) != 2:
        print("Usage: delete_command <command_name>")
        return

    persistence_dao = PersistenceManager().get_implementation()

    # Delete command from the command file
    if persistence_dao.delete_command(sys.argv[1]) == False:
        print(f"""Error: Command '{sys.argv[1]}' was not found.""")
        return

    # Delete bash script
    os.remove(f"/usr/local/bin/{sys.argv[1]}")

    print("Command '" + sys.argv[1] + "' succesfully deleted.")

if __name__ == "__main__":
    main()