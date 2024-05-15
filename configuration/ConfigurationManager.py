import os
import json

class ConfigurationManager:

    def __init__(self):
        return self

    # NEEDS REVISION
    def set_implementation(self, implementation):
        path_to_script
        with open("config.json", 'r') as config_file:
            path_to_script = json.load(config_file).get("path_to_custom_commands_history_directory")

        config_dictionary = {
            "type" : implementation,
            "path_to_custom_commands_history_directory" : path_to_script,
            "storage_file_name" : "commands_storage"
        }

        with open("config.json", 'w') as config_file:
            json.dump(config_dictionary, config_file, indent=4)

    # similar code to previous set
    def set_implementation_storage_file():
        return


    def get_implementation(self):
        with open("config.json", 'r') as config_file:
            return json.load(config_file)

    def get_storage_file_location(self):
        # do something
        return