import os
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ..models.enums.ConfigurationDefault import *
from ..models.enums.ConfigurationProperty import *

class ConfigurationManager:

    def __init__(self):
        pass

    def set_default_configuration(self):
        config_dictionary = {
            ConfigurationProperty.IMPLEMENTATION_TYPE.value : ConfigurationDefault.DEFAULT_STORAGE_FILE_NAME.value,
            ConfigurationProperty.STORAGE_FILE_NAME.value : ConfigurationDefault.DEFAULT_STORAGE_FILE_NAME.value,
            ConfigurationProperty.STORAGE_FILE_NAME.value : ConfigurationDefault.get_default_storage_file_location()
        }

        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, 'w') as config_file:
            json.dump(config_dictionary, config_file, indent=4)

    def set_configuration(self, implementation, path_to_script, storage_file_name):
        config_dictionary = {
            ConfigurationProperty.IMPLEMENTATION_TYPE.value : implementation,
            ConfigurationProperty.STORAGE_FILE_NAME.value : storage_file_name,
            ConfigurationProperty.STORAGE_FILE_NAME.value : path_to_script
        }

        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, 'w') as config_file:
            json.dump(config_dictionary, config_file, indent=4)

    def get_configuration(self):
        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, 'r') as config_file:
            return json.load(config_file)

    def get_storage_file_location(self):
        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, 'r') as config_file:
            return json.load(config_file)
