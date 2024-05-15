from enum import Enum
import os

class ConfigurationDefault(Enum):
    CONFIG_FILE_NAME = "config.json"
    DEFAULT_IMPLEMENTATION_TYPE = "JSON"
    DEFAULT_STORAGE_FILE_NAME = "storage_file_name"
    BASE_DIRECTORY = "/persistence/implementations/"
