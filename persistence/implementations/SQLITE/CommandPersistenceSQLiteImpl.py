import sqlite3
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.enums.ConfigurationProperty import *
from persistence.implementations.CommandPersistenceDao import *
from models.enums.CommandProperty import *
from models.Command import Command

# SQLite implementation of CommandPersistenceDao
class CommandPersistenceDaoSQLiteImpl(CommandPersistenceDao):

    def __init__(self, persistence_configuration):
        self.persistence_file = persistence_configuration.storage_file_path
        directory = os.path.dirname(self.persistence_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.conn = sqlite3.connect(self.persistence_file)
        self.conn.row_factory = sqlite3.Row
        self.create_table_if_not_exists()

    # Override
    def add_command(self, new_command):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO commands (command_name, path_to_bash_script, creation_date)
            VALUES (?, ?, ?)
        """, (new_command.command_name, new_command.path_to_bash_script, new_command.creation_date))
        self.conn.commit()

    # Override
    def list_commands(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM commands")
        return [self.row_to_command(row) for row in cursor.fetchall()]

    # Override
    def find_command(self, command_to_find):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM commands WHERE command_name=?", (command_to_find,))
        row = cursor.fetchone()
        if row:
            return self.row_to_command(row)
        return None

    # Override
    def delete_command(self, command_to_delete):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM commands WHERE command_name=?", (command_to_delete,))
        self.conn.commit()
        return cursor.rowcount > 0

    # Override
    def update_command(self, command_to_update, new_script):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE commands
            SET script=?
            WHERE command_name=?
        """, (new_script, command_to_update))
        self.conn.commit()
        return cursor.rowcount > 0


    # Override
    def reset_implementation(self):
        # Close the connection
        self.conn.close()
        # Remove the database file
        try:
            os.remove(self.persistence_file)
        except FileNotFoundError:
            pass
        return

    ### Utility Methods
    def create_table_if_not_exists(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command_name TEXT,
                path_to_bash_script TEXT,
                creation_date TEXT
            );
        """
        self.conn.execute(create_table_sql)

    def row_to_command(self, row):
        return Command(
            command_name=row[CommandProperty.COMMAND_NAME.value],
            path_to_bash_script=row[CommandProperty.PATH_TO_BASH_SCRIPT.value],
            creation_date=row[CommandProperty.CREATION_DATE.value]
        )

    def __del__(self):
        self.conn.close()
