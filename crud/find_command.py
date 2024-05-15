import sys
import os
from datetime import datetime

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from persistence.PersistenceManager import *
from models.Command import Command
from models.enums.CommandProperty import *

def main():
    if len(sys.argv) != 2:
        print("Usage: find_command <command_name>")
        return

    # Handling possible results of the find_command()
    maybe_command = PersistenceManager().get_implementation().find_command(sys.argv[1])
    if maybe_command == False or maybe_command == None:
        print(f"""Error: Command '{sys.argv[1]}' was not found.""")
        return

    print(f"""Command Name \t: {maybe_command.get(CommandProperty.COMMAND_NAME.value)}\n""" +
          f"""Path to Script \t: {maybe_command.get(CommandProperty.PATH_TO_PYTHON_SCRIPT.value)}\n""" +
          f"""Creation Date \t: {datetime.fromisoformat(maybe_command.get(CommandProperty.CREATION_DATE.value))}""")

if __name__ == "__main__":
    main()