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
    path_to_script = sys.argv[2]
    path_to_bin_script = f"/usr/local/bin/{command_name}"

    try:
        if not os.path.exists(path_to_script):
            print(f"The script '{path_to_script}' does not exist.")
            return

        # Copy user script to bin directory
        with open(path_to_script, FilePermission.READ.value) as user_script:
            with open(path_to_bin_script, FilePermission.WRITE.value) as bin_script:
                shutil.copyfileobj(user_script, bin_script)

        os.chmod(path_to_bin_script, 0o755)

    except PermissionError:
        print("This command requires sudo privileges.")
        return

    # Add the new command to the command file
    datetimeiso = datetime.now().isoformat()
    command = Command(
        command_name,
        path_to_bin_script,
        datetimeiso
    )
    PersistenceManager().get_implementation().add_command(command)

    print("Command '" + sys.argv[1] + "' succesfully created.")

if __name__ == "__main__":
    main()
