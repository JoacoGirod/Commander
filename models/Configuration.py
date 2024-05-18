import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.enums.ConfigurationDefault import *
from models.enums.ConfigurationProperty import *
from models.enums.FilePermission import *

class Configuration:
    def __init__(self, implementation_type, storage_file_name, storage_file_dir, storage_file_path):
        self.implementation_type = implementation_type
        self.storage_file_name = storage_file_name
        self.storage_file_dir = storage_file_dir
        self.storage_file_path = storage_file_path

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_data = json.loads(json_str)
        return cls(**json_data)

    def get_instance_as_dictionary(self):
        return self.__dict__

    def __str__(self):
        return f"<Implementation Type='{self.implementation_type}', Storage File Name ='{self.storage_file_path}', Storage File Dir ='{self.storage_file_dir}', Storage File Location ='{self.storage_file_path}'>"

    @classmethod
    def default_instance(cls):
        default_storage_file_path = os.getcwd() + ConfigurationDefault.DEFAULT_STORAGE_DIR.value + ConfigurationDefault.DEFAULT_IMPLEMENTATION_TYPE.value + "/" + ConfigurationDefault.DEFAULT_STORAGE_FILE_NAME.value + "." + ConfigurationDefault.DEFAULT_IMPLEMENTATION_TYPE.value.lower()
        return cls(
            ConfigurationDefault.DEFAULT_IMPLEMENTATION_TYPE.value,
            ConfigurationDefault.DEFAULT_STORAGE_FILE_NAME.value,
            ConfigurationDefault.DEFAULT_STORAGE_DIR.value,
            default_storage_file_path
        )