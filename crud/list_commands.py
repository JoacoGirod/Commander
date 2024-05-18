import os
import sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from persistence.PersistenceManager import *

def main():
    if len(sys.argv) > 2:
        print("Usage: list_commands [-a]")
        return

    persistence_dao = PersistenceManager().get_implementation()

    # Handle '-a' flag
    if len(sys.argv) == 2:
        if  sys.argv[1] == '-a':
            command_list = '\n'.join([f"Command Name : '{command.command_name}', Path To Bash Script : '{command.path_to_bash_script}', Path To Python Script : '{command.path_to_python_script}', Date of Creation '{datetime.fromisoformat(command.creation_date)}'" for command in persistence_dao.list_commands()])
    else:
        command_list = '\n'.join([f"{cmd.command_name}" for cmd in persistence_dao.list_commands()])

    print(command_list)

if __name__ == "__main__":
    main()