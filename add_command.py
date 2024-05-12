# addCommand.py
import json
import sys
import os
from CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl
from Command import Command
from datetime import datetime

# ! Should be configurable, persistance, path to the custom_commands

def main():
    if len(sys.argv) != 3:
        print("Usage: addCommand <command_name> <absolute_path_to_python_script>")
        return

    with open("config.json", 'r') as config_file:
        config = json.loads(config_file.read())

    # ! Should somehow be interchageable?
    persistance_dao = CommandPersistenceDaoJsonImpl(config.get("persistence"))
    command = Command(sys.argv[1], sys.argv[2], datetime.now().isoformat())


    print(command)

    # # Create a bash script in /usr/local/bin
    # bash_script_content = f"""#!/bin/bash
    #     python3 {command.path_to_script} "$@"
    #     """
    # bash_script_path = f"/usr/local/bin/{command.command_name}"
    # with open(bash_script_path, 'w') as script_file:
    #     script_file.write(bash_script_content)

    # # Set execute permissions
    # os.chmod(bash_script_path, 0o755)

    # Add the new command to the command file
    persistance_dao.add_command(command)

    print("Command " + command.command_name + " succesfully created!")

if __name__ == "__main__":
    main()
