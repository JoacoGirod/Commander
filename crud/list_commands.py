import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl

def main():
    if len(sys.argv) > 2:
        print("Usage: list_commands [-a]")
        return

    # Get Persistence Strategy from Config File
    with open("config.json", 'r') as config_file:
        config = json.loads(config_file.read())

    persistance_dao = CommandPersistenceDaoJsonImpl(config.get("persistence"))

    if len(sys.argv) == 2:
        if  sys.argv[1] == '-a':
            command_list = '\n'.join([f"Command <{cmd['command_name']}> || Path <{cmd['path_to_script']}> || Creation Date <{cmd['creation_date']}>" for cmd in persistance_dao.list_commands()])
    else:
        command_list = '\n'.join([f"<{cmd['command_name']}>" for cmd in persistance_dao.list_commands()])

    print(command_list)

if __name__ == "__main__":
    main()