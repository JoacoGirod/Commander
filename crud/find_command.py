import sys
import os
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.PersistenceManager import *
from models.Command import Command

def main():
    if len(sys.argv) != 2:
        print("Usage: find_command <command_name>")
        return

    # Handling possible results of the find_command()
    maybe_command = PersistenceManager().get_implementation().find_command(sys.argv[1])
    if maybe_command == False or maybe_command == None:
        print(f"""Error: Command '{sys.argv[1]}' was not found.""")
        return

    print(f"""Command Name : {maybe_command.get("command_name")} \nPath to Script : {maybe_command.get("path_to_script")}\nDate of Creation : {datetime.fromisoformat(maybe_command.get("creation_date"))}""")

if __name__ == "__main__":
    main()