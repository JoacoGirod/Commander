import yaml

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from configuration.ConfigurationManager import *
from persistence.implementations.CommandPersistenceDao import CommandPersistenceDao
from models.enums.ConfigurationProperty import *
from models.enums.CommandProperty import *
from models.enums.FilePermission import *
from models.Command import Command

class CommandPersistenceDaoYamlImpl(CommandPersistenceDao):

    def __init__(self, persistence_configuration):
        self.persistence_file = persistence_configuration.get(ConfigurationProperty.STORAGE_FILE_LOCATION.value)

    # Override
    def add_command(self, new_command):
        commands = self.load_commands()
        commands.append(new_command.get_instance_as_dictionary())  # Assuming get_instance_as_dictionary() returns a dictionary
        self.save_commands(self.persistence_file, commands)

    # Override
    def list_commands(self):
        commands = self.load_commands()
        command_list = []
        for command_data in commands:
            command_list.append(Command(
                command_name=command_data.get(CommandProperty.COMMAND_NAME.value),
                path_to_python_script=command_data.get(CommandProperty.PATH_TO_PYTHON_SCRIPT.value),
                path_to_bash_script=command_data.get(CommandProperty.PATH_TO_BASH_SCRIPT.value),
                creation_date=command_data.get(CommandProperty.CREATION_DATE.value)
            ))
        return command_list

    # Override
    def find_command(self, command_to_find):
        commands = self.load_commands()
        for command in commands:
            if command.get(CommandProperty.COMMAND_NAME.value) == command_to_find:
                return Command(
                    command_name=command.get(CommandProperty.COMMAND_NAME.value),
                    path_to_python_script=command.get(CommandProperty.PATH_TO_PYTHON_SCRIPT.value),
                    path_to_bash_script=command.get(CommandProperty.PATH_TO_BASH_SCRIPT.value),
                    creation_date=command.get(CommandProperty.CREATION_DATE.value)
                )
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
    # Override
    def reset_implementation(self):
        # Remove files created in /usr/local/bin
        for command in self.load_commands():
            try:
                os.remove(command.get(CommandProperty.PATH_TO_BASH_SCRIPT.value))
            except FileNotFoundError:
                pass
        # Remove storage File
        try:
            os.remove(ConfigurationManager().get_configuration().get(ConfigurationProperty.STORAGE_FILE_LOCATION.value))
        except FileNotFoundError:
            pass
        return


    ### Utility Methods
    def load_commands(self):
        try:
            with open(self.persistence_file, FilePermission.READ.value) as file:
                file_content = file.read()
                if not file_content:
                    return []
                return yaml.safe_load(file_content)
        except FileNotFoundError:
            return []

    def save_commands(self, filename, commands):
        with open(filename, FilePermission.WRITE.value) as file:
            yaml.dump(commands, file)
