import json
import os

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.enums.ConfigurationDefault import *
from models.enums.ConfigurationProperty import *


class ConfigurationManager:

    def __init__(self):
        pass

    def set_default_configuration(self):
        config_dictionary = {
            ConfigurationProperty.IMPLEMENTATION_TYPE.value : ConfigurationDefault.DEFAULT_IMPLEMENTATION_TYPE.value,
            ConfigurationProperty.STORAGE_FILE_NAME.value : ConfigurationDefault.DEFAULT_STORAGE_FILE_NAME.value,
            ConfigurationProperty.STORAGE_FILE_LOCATION.value : os.getcwd() + ConfigurationDefault.BASE_DIRECTORY.value + ConfigurationDefault.DEFAULT_STORAGE_FILE_NAME.value
        }

        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, 'w') as config_file:
            json.dump(config_dictionary, config_file, indent=4)

    def set_configuration(self, implementation, path_to_script, storage_file_name):
        config_dictionary = {
            ConfigurationProperty.IMPLEMENTATION_TYPE.value : implementation,
            ConfigurationProperty.STORAGE_FILE_NAME.value : storage_file_name,
            ConfigurationProperty.STORAGE_FILE_LOCATION.value : path_to_script
        }

        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, 'w') as config_file:
            json.dump(config_dictionary, config_file, indent=4)

    def get_configuration(self):
        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, 'r') as config_file:
            return json.load(config_file)
