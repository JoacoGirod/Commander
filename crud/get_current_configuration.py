import sys
import os
from datetime import datetime

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from configuration.ConfigurationManager import *
from models.Command import Command
from models.enums.CommandProperty import *

def main():
    if len(sys.argv) != 1:
        print("Usage: get_current_configuration")
        return

    current_configuration = ConfigurationManager().get_configuration()

    print(
        f"""Persistence Strategy \t: {current_configuration.implementation_type}\n"""
        f"""Storage File Name \t: {current_configuration.storage_file_name}\n"""
        f"""Storage File Dir \t: {current_configuration.storage_file_dir}\n"""
        f"""Storage File Path \t: {current_configuration.storage_file_path}"""
    )

if __name__ == "__main__":
    main()