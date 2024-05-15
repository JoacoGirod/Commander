from enum import Enum

class CommandProperty(Enum):
    COMMAND_NAME = "command_name"
    PATH_TO_PYTHON_SCRIPT = "path_to_python_script"
    PATH_TO_BASH_SCRIPT = "path_to_bash_script"
    CREATION_DATE = "creation_date"