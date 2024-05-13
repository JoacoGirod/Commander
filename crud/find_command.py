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
    persistence_dao = CommandPersistenceDaoJsonImpl(config)

    # Functionality
    maybe_command = persistence_dao.find_command(sys.argv[1])
    if maybe_command == False or maybe_command == None:
        print(f"""Error: Command '{sys.argv[1]}' was not found.""")
        return

    print(f"""Command Name : {maybe_command.get("command_name")} \nPath to Script : {maybe_command.get("path_to_script")}\nDate of Creation : {datetime.fromisoformat(maybe_command.get("creation_date"))}""")

if __name__ == "__main__":
    main()