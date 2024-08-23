from enum import Enum

class PersistenceImplementation(Enum):
    JSON = "JSON"
    YAML = "YAML"
    SQLITE = "SQLITE"
