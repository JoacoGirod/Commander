import sys
import os
from datetime import datetime
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from configuration.ConfigurationManager import *
from models.Command import Command
from models.enums.CommandProperty import *

def main():
    if len(sys.argv) != 1:
        print("Usage: list_local_commands")
        return

    completed_process = subprocess.run(["ls", "/usr/local/bin"], capture_output=True, text=True)
    print(completed_process.stdout)

if __name__ == "__main__":
    main()
