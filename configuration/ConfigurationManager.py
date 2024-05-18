import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.enums.ConfigurationDefault import *
from models.enums.ConfigurationProperty import *
from models.enums.FilePermission import *
from models.Configuration import Configuration

class ConfigurationManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        pass

    def set_default_configuration(self):
        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, FilePermission.WRITE.value) as config_file:
            json.dump(Configuration.default_instance().get_instance_as_dictionary(), config_file, indent=4)

    def set_configuration(self, implementation, storage_file_name, storage_file_dir, storage_file_path):
        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, FilePermission.WRITE.value) as config_file:
            json.dump(Configuration(implementation, storage_file_name, storage_file_dir, storage_file_path).get_instance_as_dictionary(), config_file, indent=4)

    def get_configuration(self):
        with open(ConfigurationDefault.CONFIG_FILE_NAME.value, FilePermission.READ.value) as config_file:
            config_dict = json.load(config_file)
            return Configuration(
                config_dict.get(ConfigurationProperty.IMPLEMENTATION_TYPE.value),
                config_dict.get(ConfigurationProperty.STORAGE_FILE_NAME.value),
                config_dict.get(ConfigurationProperty.STORAGE_FILE_DIR.value),
                config_dict.get(ConfigurationProperty.STORAGE_FILE_PATH.value),
            )

    def delete_configuration(self):
        os.remove(ConfigurationDefault.CONFIG_FILE_NAME.value)
