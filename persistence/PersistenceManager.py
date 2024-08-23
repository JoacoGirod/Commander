import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from persistence.PersistenceManager import *
from models.Command import Command
from persistence.implementations.JSON.CommandPersistenceDaoJsonImpl import CommandPersistenceDaoJsonImpl
from persistence.implementations.YAML.CommandPersistenceDaoYamlImpl import CommandPersistenceDaoYamlImpl
from persistence.implementations.SQLITE.CommandPersistenceSQLiteImpl import CommandPersistenceDaoSQLiteImpl
from configuration.ConfigurationManager import *
from models.enums.PersistenceImplementation import *

class PersistenceManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PersistenceManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.config = ConfigurationManager().get_configuration()

    def get_implementation(self):
        if self.config.implementation_type == PersistenceImplementation.JSON.value:
            return CommandPersistenceDaoJsonImpl(self.config)
        elif self.config.implementation_type == PersistenceImplementation.YAML.value:
            return CommandPersistenceDaoYamlImpl(self.config)
        elif self.config.implementation_type == PersistenceImplementation.SQLITE.value:
            persistence_strategy = CommandPersistenceDaoSQLiteImpl(self.config)
            persistence_strategy.create_table_if_not_exists()
            return persistence_strategy

    def get_json_implementation(self):
        return CommandPersistenceDaoJsonImpl(self.config)

    def get_yaml_implementation(self):
        return CommandPersistenceDaoYamlImpl(self.config)

    def get_sqlite_implementation(self):
        persistence_strategy = CommandPersistenceDaoSQLiteImpl(self.config)
        persistence_strategy.create_table_if_not_exists()
        return persistence_strategy

    def shift_implementation(self, new_implementation):
        initial_configuration = ConfigurationManager().get_configuration()
        initial_implementation = self.get_implementation()
        ConfigurationManager().set_configuration(new_implementation, initial_configuration.storage_file_name, initial_configuration.storage_file_dir, initial_configuration.storage_file_path)
        final_implementation = self.get_implementation()

        for command in initial_implementation.list_commands():
            final_implementation.add_command(command)

        initial_implementation.reset_implementation()
