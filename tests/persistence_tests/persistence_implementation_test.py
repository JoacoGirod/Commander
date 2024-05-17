import unittest
from datetime import datetime
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(PARENT_DIR)
sys.path.append(ROOT_DIR)

from persistence.PersistenceManager import *
from models.enums.CommandProperty import *
from models.Command import *

# These are not pure unit tests, the different methods test each other
# Adequate unit tests should acommodate preconditions to each implementation
class TestPersistenceImplementation(unittest.TestCase):

    def setUp(self):
        self.persistence_implementation = PersistenceManager().get_implementation()
        self.command_name = "test_command"
        self.non_existent_command_name = "non_existent_command_name"
        self.python_command_path = "/path/to/python/command"
        self.bash_command_path = "/path/to/bash/command"
        self.updated_python_path = "/path/to/updated/python/command"
        self.updated_bash_path = "/path/to/updated/bash/command"
        self.command_date_of_creation = datetime.now().isoformat()

    def tearDown(self):
            self.persistence_implementation.reset_implementation()
            pass
    def test_add_command(self):
        # Preconditions
        initial_length = len(self.persistence_implementation.list_commands())
        new_command = Command(self.command_name, self.python_command_path, self.bash_command_path, self.command_date_of_creation)

        # Evaluation
        self.persistence_implementation.add_command(new_command)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length + 1)
        created_command = self.persistence_implementation.find_command(self.command_name)
        self.assertEqual(self.command_name, created_command.command_name)
        self.assertEqual(self.python_command_path, created_command.path_to_python_script)
        self.assertEqual(self.bash_command_path, created_command.path_to_bash_script)
        self.assertEqual(self.command_date_of_creation, created_command.creation_date)

    def test_fail_find_command(self):
        # Evaluation
        found_command = self.persistence_implementation.find_command(self.non_existent_command_name)

        # Postconditions & Validations
        self.assertEqual(found_command, None)

    def test_delete_command(self):
        # Preconditions
        new_command = Command(self.command_name, self.python_command_path, self.bash_command_path, self.command_date_of_creation)
        self.persistence_implementation.add_command(new_command)
        initial_length = len(self.persistence_implementation.list_commands())

        # Evaluation
        deleted = self.persistence_implementation.delete_command(self.command_name)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertTrue(deleted)
        self.assertEqual(final_length, initial_length - 1)

    def test_fail_delete_command(self):
        # Preconditions
        initial_length = len(self.persistence_implementation.list_commands())

        # Evaluation
        deleted = self.persistence_implementation.delete_command(self.non_existent_command_name)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length)
        self.assertFalse(deleted)


    def test_update_command(self):
        # Preconditions
        new_command = Command(self.command_name, self.python_command_path, self.bash_command_path, self.command_date_of_creation)
        self.persistence_implementation.add_command(new_command)
        initial_length = len(self.persistence_implementation.list_commands())

        # Evaluation
        updated = self.persistence_implementation.update_command(self.command_name, self.updated_python_path)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length)
        self.assertTrue(updated)

    def test_fail_update_command(self):
        # Preconditions
        initial_length = len(self.persistence_implementation.list_commands())

        # Evaluation
        updated = self.persistence_implementation.update_command(self.non_existent_command_name, self.updated_python_path)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length)
        self.assertFalse(updated)


if __name__ == '__main__':
    unittest.main()
