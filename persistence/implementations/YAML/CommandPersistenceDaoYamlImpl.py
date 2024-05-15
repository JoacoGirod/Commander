import yaml
from persistence.implementations.CommandPersistenceDao import CommandPersistenceDao

class CommandPersistenceDaoYamlImpl(CommandPersistenceDao):

    def __init__(self, persistence_configuration):
        self.persistence_file = persistence_configuration.get("path_to_custom_commands_history_directory") + persistence_configuration.get("storage_file_name")

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
            if command.get("command_name") == command_to_find:
                return command
        return None

    # Override
    def delete_command(self, command_to_delete):
        commands = self.load_commands()
        for command in commands:
            if command.get("command_name") == command_to_delete:
                commands.remove(command)
                self.save_commands(self.persistence_file, commands)
                return True
        return False

    # Override
    def update_command(self, command_to_update, new_path):
        commands = self.load_commands()
        for command in commands:
            if command.get("command_name") == command_to_update:
                command["path_to_script"] = new_path
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
