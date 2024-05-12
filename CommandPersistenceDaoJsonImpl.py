import json
from CommandPersistenceDao import *

# Implementing the interface
class CommandPersistenceDaoJsonImpl(CommandPersistenceDao):

    def __init__(self, persistence_configuration):
        if persistence_configuration.get("type") != 'json':
            print("Implementation manages JSON but configuration specifies " + persistence_configuration.type + " as persistence type")
            print(persistence_configuration)
            return
        self.persistence_file = persistence_configuration.get("path_to_custom_commands_history")


    # def add_command(self, new_command):
    #     commands = self.load_commands()
    #     if not commands:  # Check if commands is empty
    #         commands = [new_command]  # Initialize commands with new_command
    #     else:
    #         commands.append(new_command)  # Append new_command to existing commands
    #     self.save_commands(self.persistence_file, commands)

    # Override
    def add_command(self, new_command):
        commands = self.load_commands()
        print(commands)
        commands.append(new_command.get_instance_as_dictionary())
        print(commands)
        self.save_commands(self.persistence_file, commands)

    # Override
    def list_commands(self):
        return self.load_commands

    # Override
    def delete_command(self, command_to_delete):
        return


    ### Utility Methods
    def load_commands(self):
        try:
            with open(self.persistence_file, 'r') as file:
                file_content = file.read()
                if not file_content:
                    return []
                return json.loads(file_content)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def save_commands(self, filename, commands):
        with open(filename, 'w') as file:
            json.dump(commands, file, indent=4)
