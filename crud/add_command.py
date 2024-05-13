import json
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Command import Command
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl

def main():
    if len(sys.argv) != 3:
        print("Usage: add_command <command_name> <absolute_path_to_python_script>")
        return

    # Get Persistence Strategy from Config File
    with open(os.getcwd() + "/config.json", 'r') as config_file:
        config = json.loads(config_file.read())

    persistence_dao = CommandPersistenceDaoJsonImpl(config)
    command = Command(sys.argv[1], sys.argv[2], datetime.now().isoformat())

    # Create a bash script in /usr/local/bin
    bash_script_content =   f"""
                            #!/bin/bash
                            python3 {command.path_to_script} "$@"
                            """
    bash_script_path =      f"/usr/local/bin/{command.command_name}"
    with open(bash_script_path, 'w') as script_file:
        script_file.write(bash_script_content)
    os.chmod(bash_script_path, 0o755)

    # Add the new command to the command file
    persistence_dao.add_command(command)

    print("Command '" + command.command_name + "' succesfully created.")

if __name__ == "__main__":
    main()
