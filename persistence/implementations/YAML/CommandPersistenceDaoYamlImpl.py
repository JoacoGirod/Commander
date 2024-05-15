import yaml

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.enums.ConfigurationProperty import *
from persistence.implementations.CommandPersistenceDao import CommandPersistenceDao
from models.enums.CommandProperty import *

class CommandPersistenceDaoYamlImpl(CommandPersistenceDao):

    def __init__(self, persistence_configuration):
        self.persistence_file = persistence_configuration.get(ConfigurationProperty.STORAGE_FILE_LOCATION.value) + "/" + persistence_configuration.get(ConfigurationProperty.STORAGE_FILE_NAME.value)

    # Override
    def add_command(self, new_command):
        commands = self.load_commands()
        commands.append(new_command.get_instance_as_dictionary())  # Assuming get_instance_as_dictionary() returns a dictionary
        self.save_commands(self.persistence_file, commands)

    # Override
    def list_commands(self):
        return self.load_commands()

    # Override
    def find_command(self, command_to_find):
        commands = self.load_commands()
        for command in commands:
            if command.get(CommandProperty.COMMAND_NAME.value) == command_to_find:
                return command
        return None

    # Override
    def delete_command(self, command_to_delete):
        commands = self.load_commands()
        for command in commands:
            if command.get(CommandProperty.COMMAND_NAME.value) == command_to_delete:
                commands.remove(command)
                self.save_commands(self.persistence_file, commands)
                return True
        return False

    # Override
    def update_command(self, command_to_update, new_path):
        commands = self.load_commands()
        for command in commands:
            if command.get(CommandProperty.COMMAND_NAME.value) == command_to_update:
                command[CommandProperty.PATH_TO_PYTHON_SCRIPT.value] = new_path
                self.save_commands(self.persistence_file, commands)
                return True
        return False

    # Override
    def reset_implementation():
        return

    ### Utility Methods
    def load_commands(self):
        try:
            with open(self.persistence_file, 'r') as file:
                file_content = file.read()
                if not file_content:
                    return []
                return yaml.safe_load(file_content)
        except FileNotFoundError:
            return []

    def save_commands(self, filename, commands):
        with open(filename, 'w') as file:
            yaml.dump(commands, file)
