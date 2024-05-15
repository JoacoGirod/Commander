import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from persistence.PersistenceManager import *
from models.Command import Command
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import *
from persistence.implementations.YAML.CommandPersistenceDaoYamlImpl import *
from persistence.implementations.SQLite.CommandPersistenceSQLiteImpl import *
from configuration.ConfigurationManager import *
from models.enums.PersistenceImplementation import *

class PersistenceManager:
    def __init__(self):
        self.config = ConfigurationManager().get_configuration()

    def get_implementation(self):
        if (self.config.get(ConfigurationProperty.IMPLEMENTATION_TYPE.value) == PersistenceImplementation.JSON.value):
            return CommandPersistenceDaoJsonImpl(self.config)
        if (self.config.get(ConfigurationProperty.IMPLEMENTATION_TYPE.value) == PersistenceImplementation.YAML.value):
            return CommandPersistenceDaoYamlImpl(self.config)
        if (self.config.get(ConfigurationProperty.IMPLEMENTATION_TYPE.value) == PersistenceImplementation.SQLITE.value):
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
        ConfigurationManager.set_configuration(new_implementation)
        final_implementation = self.get_implementation()

        for command_names in initial_implementation.list_commands():
            command = initial_implementation.find_command(command_names)
            final_implementation.add_command(command)

        initial_implementation.reset_
