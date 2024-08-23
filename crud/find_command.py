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
        print(f"Error: Command '{sys.argv[1]}' was not found.")
        return

    print(f"Command Name \t\t: {maybe_command.command_name}\n" +
          f"Path to Bash/Python Script \t: {maybe_command.path_to_python_or_bash_script}\n" +
          f"Path to Caller Bash Script \t: {maybe_command.path_to_bash_script}\n" +
          f"Creation Date \t\t: {datetime.fromisoformat(maybe_command.creation_date)}")

if __name__ == "__main__":
    main()