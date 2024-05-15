# Should install the 4 basic commands, add delete list find
#### Installer
# 1. Ask for configuration values and write the JSON
# 2. Install the add_command
# 3. Use add_command to add the other main commands
# 4. Should somehow add to the history the add_command which would be omitted
import subprocess
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .configuration.ConfigurationManager import *

def main():
    # These are statically defined but input() could be used to configure them
    # Options are JSON, YAML, SQLite
    persistence_type = "JSON"
    cwd = os.getcwd()
    storing_file = cwd + "/persistence/implementations/" + persistence_type + "/"

    ConfigurationManager().set_implementation(persistence_type, storing_file)

    # Create config.json
    config_dictionary = {
        "type" : persistence_type,
        "path_to_custom_commands_history_directory" : storing_file,
        "history_file_name" : "custom_commands.db"
    }

    with open("config.json", 'w') as config_file:
        json.dump(config_dictionary, config_file, indent=4)

    # Install Initial Commands
    for command in ["add_command", "delete_command", "find_command", "list_commands", "update_command"]:
        result = subprocess.run(
             f"sudo python3 ./crud/add_command.py {command} {cwd}/crud/{command}.py"
             , shell=True, capture_output=True, text=True, cwd=cwd
        )
        if result.returncode == 0:
            print(f"{command} installed successfully!")
        else:
            print(f"Error installing {command}:")
            print(result.stderr)

    print("\nInfo : Using add_command, update_command and delete_command requires sudo privileges.")

if __name__ == "__main__":
    main()
