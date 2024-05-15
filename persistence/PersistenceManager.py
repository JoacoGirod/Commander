import json
import os
from .implementations.JSON.CommandPersistenceDaoJsonImpl import *
from .implementations.YAML.CommandPersistenceDaoYamlImpl import *
from .implementations.SQLite.CommandPersistenceSQLiteImpl import *
from ..configuration.ConfigurationManager import *

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

    def get_json_implementation(self):
        return CommandPersistenceDaoJsonImpl(self.config)

    def get_yaml_implementation(self):
        return CommandPersistenceDaoJsonImpl(self.config)

    def get_sqlite_implementation(self):
        persistence_strategy = CommandPersistenceDaoSQLiteImpl(self.config)
        persistence_strategy.create_table_if_not_exists()
        return persistence_strategy

    # Should transfer all the information in one implementation to the other
    # Shouldnt be that hard as the persistence modules all use dictionary returns, and dictionary inputs for creation
    def shift_implementation(self, new_implementation):
        initial_implementation = self.get_implementation()
        ConfigurationManager.set_implementation(new_implementation)
        final_implementation = self.get_implementation()

        for command_names in initial_implementation.list_commands():
            command = initial_implementation.find_command(command_names)
            final_implementation.add_command(command)

        initial_implementation.reset_
