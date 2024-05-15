import sqlite3

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.enums.ConfigurationProperty import *
from persistence.implementations.CommandPersistenceDao import *

# SQLite implementation of CommandPersistenceDao
class CommandPersistenceDaoSQLiteImpl(CommandPersistenceDao):

    def __init__(self, persistence_configuration):
        self.persistence_file = persistence_configuration.get(ConfigurationProperty.STORAGE_FILE_LOCATION.value) + "/" + persistence_configuration.get(ConfigurationProperty.STORAGE_FILE_NAME.value)
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row
        self.create_table_if_not_exists()

    # Override
    def add_command(self, new_command):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO commands (command_name, path_to_script, creation_date)
            VALUES (?, ?, ?)
        """, (new_command.command_name, new_command.path_to_script, new_command.creation_date))
        self.conn.commit()

    # Override
    def list_commands(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM commands")
        return [dict(row) for row in cursor.fetchall()]

    # Override
    def find_command(self, command_to_find):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM commands WHERE command_name=?", (command_to_find,))
        return dict(cursor.fetchone())

    # Override
    def delete_command(self, command_to_delete):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM commands WHERE command_name=?", (command_to_delete,))
        self.conn.commit()

    # Override
    def update_command(self, command_to_update, new_path):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE commands SET path_to_script=? WHERE command_name=?", (new_path, command_to_update))
        self.conn.commit()

    # Override
    def reset_implementation():
        return

    ### Utility Methods
    def create_table_if_not_exists(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command_name TEXT,
                path_to_script TEXT,
                creation_date TEXT
            );
        """
        self.conn.execute(create_table_sql)

    def __del__(self):
        self.conn.close()
