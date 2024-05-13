import os
import sys
import json
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl

def main():
    if len(sys.argv) > 2:
        print("Usage: list_commands [-a]")
        return

    # Get Persistence Strategy from Config File
    with open("config.json", 'r') as config_file:
        config = json.loads(config_file.read())
    persistence_dao = CommandPersistenceDaoJsonImpl(config)

    if len(sys.argv) == 2:
        if  sys.argv[1] == '-a':
            command_list = '\n'.join([f"Command Name : '{command['command_name']}', Path To Script : '{command['path_to_script']}' || Date of Creation '{datetime.fromisoformat(command['creation_date'])}'" for command in persistence_dao.list_commands()])
    else:
        command_list = '\n'.join([f"{cmd['command_name']}" for cmd in persistence_dao.list_commands()])

    print(command_list)

if __name__ == "__main__":
    main()