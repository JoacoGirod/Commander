import json
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.PersistenceManager import *
from models.Command import Command
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl

def main():
    if len(sys.argv) != 3:
        print("Usage: add_command <command_name> <absolute_path_to_python_script>")
        return

    # Create a bash script in /usr/local/bin
    bash_script_content =   f"""
                            #!/bin/bash
                            python3 {sys.argv[2]} "$@"
                            """
    bash_script_path =      f"/usr/local/bin/{sys.argv[1]}"

    with open(bash_script_path, 'w') as script_file:
        script_file.write(bash_script_content)
    os.chmod(bash_script_path, 0o755)

    # Add the new command to the command file
    PersistenceManager().get_implementation().add_command(
        Command(sys.argv[1], sys.argv[2], bash_script_path, datetime.now().isoformat())
    )

    print("Command '" + sys.argv[1] + "' succesfully created.")

if __name__ == "__main__":
    main()
