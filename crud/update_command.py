import json
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Command import Command
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl

def main():
    if len(sys.argv) != 3:
        print("Usage: update_command <command_name> <new_path>")
        return

    # Get Persistence Strategy from Config File
    with open("config.json", 'r') as config_file:
        config = json.loads(config_file.read())
    persistence_dao = CommandPersistenceDaoJsonImpl(config)

    # Add the new command to the command file
    if persistence_dao.update_command(sys.argv[1], sys.argv[2]):
        print("Command '" + sys.argv[1] + "' updated succesfully.")
    else:
        print(f"""Error: Command '{sys.argv[1]}' was not found.""")

if __name__ == "__main__":
    main()