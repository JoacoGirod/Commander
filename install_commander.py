# Should install the 4 basic commands, add delete list find
#### Installer
# 1. Ask for configuration values and write the JSON
# 2. Install the add_command
# 3. Use add_command to add the other main commands
# 4. Should somehow add to the history the add_command which would be omitted
import subprocess
import os

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from configuration.ConfigurationManager import *

def main():
    # Create the config.json
    ConfigurationManager().set_default_configuration()

    cwd = os.getcwd()

    # Install Initial Commands
    for command in ["add_command", "delete_command", "find_command", "list_commands", "update_command", "erase_all_commands", "get_current_configuration", "list_local_commands"]:
        result = subprocess.run(
             f"sudo python3 ./crud/add_command.py {command} {cwd}/crud/{command}.py"
             , shell=True, capture_output=True, text=True, cwd=cwd
        )
        if result.returncode == 0:
            print(f"{command} installed successfully!")
        else:
            print(f"Error installing {command}:")
            print(result.stderr)

    print("\nInfo : Using add_command, update_command, delete_command and erase_all_commands requires sudo privileges.")

if __name__ == "__main__":
    main()
