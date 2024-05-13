import json
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Command import Command
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl

def main():
    if len(sys.argv) != 2:
        print("Usage: find_command <command_name>")
        return

    # Get Persistence Strategy from Config File
    with open("config.json", 'r') as config_file:
        config = json.loads(config_file.read())
    persistance_dao = CommandPersistenceDaoJsonImpl(config.get("persistence"))

    # Add the new command to the command file
    persistance_dao.find_command(sys.argv[1])

if __name__ == "__main__":
    main()