import json
import os
from .implementations.JSON.CommandPersistenceDaoJsonImpl import *
from .implementations.YAML.CommandPersistenceDaoYamlImpl import *
from .implementations.SQLite.CommandPersistenceSQLiteImpl import *


class PersistenceManager:
    def __init__(self):
        with open(os.getcwd() + "/config.json", 'r') as config_file:
            self.config = json.loads(config_file.read())

    def get_implementation(self):
        if (self.config.get("type") == "JSON"):
            return CommandPersistenceDaoJsonImpl(self.config)
        if (self.config.get("type") == "YAML"):
            return CommandPersistenceDaoYamlImpl(self.config)
        if (self.config.get("type") == "SQLite"):
            persistence_strategy = CommandPersistenceDaoSQLiteImpl(self.config)
            persistence_strategy.create_table_if_not_exists()
            return persistence_strategy

    # Should delete all traces of the implementation
    # Includes:
    # Bash scripts that the implementation was in charge of
    # Persistence structures used
    def reset_implementation():
        return

    # Should transfer all the information in one implementation to the other
    # Shouldnt be that hard as the persistence modules all use dictionary returns, and dictionary inputs for creation
    def shift_implementation():
        return