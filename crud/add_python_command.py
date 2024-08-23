import sys
import os
from datetime import datetime
import shutil
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.Command import Command
from models.enums.FilePermission import *
from persistence.PersistenceManager import *

def main():
    if len(sys.argv) != 3:
        print("Usage: add_command <command_name> <path_to_script>")
        return

    command_name = sys.argv[1]
    path_to_python_script = sys.argv[2]
    path_to_bin_script = f"/usr/local/bin/{sys.argv[1]}"

    # Copy contents of python file into another place
    # Reference the copy instead of the user script, so he can move it or delete it if he pleases

    # Create a bash script in /usr/local/bin that simply calls the python file
    bash_script_path =      f"/usr/local/bin/{command_name}"
    bash_script_content =   f"""
                            #!/bin/bash
                            python3 {path_to_python_script} "$@"
                            """

    try:
        with open(bash_script_path, FilePermission.WRITE.value) as script_file:
            script_file.write(bash_script_content)
        os.chmod(bash_script_path, 0o755)

    except PermissionError:
        print("This command requires sudo privileges.")
        return

    # Add the new command to the command file
    # THIS SHOULD CREATE A PYTHON COMMAND OBJECT AND THE PERSISTANCE MANAGER SHOULD HANDLE THE ADD PYTHON COMMAND
    # datetimeiso = datetime.now().isoformat()
    # command = Command(
    #     sys.argv[1],
    #     sys.argv[2],
    #     path_to_bin_script,
    #     datetimeiso
    # )
    # PersistenceManager().get_implementation().add_command(command)

    print("Command '" + sys.argv[1] + "' succesfully created.")

if __name__ == "__main__":
    main()
