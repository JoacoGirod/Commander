import unittest
import datetime
from ...models.Command import *
from ...persistence.PersistenceManager import *

# another script should change configuration and run this test for each implementation (JSON, YAML, SQLite)
# the test should always test the same functionalities that the interface contract obliges to

# SQLite doesnt return false when deletion was not performed

# These are not pure unit tests, the different methods test each other
# Adequate unit tests should acommodate preconditions to each implementation
class TestPersistenceImplementations(unittest.TestCase):

    def __init__(self):
        self.persistence_implementation = PersistenceManager().get_implementation()
        self.command_name = "test_command"
        self.non_existent_command_name = "non_existent_command_name"
        self.command_path = "/path/to/command"
        self.udpated_path = "/path/to/updated_command"
        self.command_date_of_creation = datetime.now().isoformat()

    def test_add_command(self):
        # Preconditions
        initial_length = len(self.persistence_implementation.list_commands())
        new_command = Command(self.command_name, self.command_path, self.command_date_of_creation)

        # Evaluation
        self.persistence_implementation.add_command(new_command)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length + 1)
        created_command = self.persistence_implementation.find_command(self.command_name)
        self.assertEqual(self.command_name, created_command.get("command_name"))
        self.assertEqual(self.command_path, created_command.get("path_to_script"))
        self.assertEqual(self.command_date_of_creation, created_command.get("creation_date"))

    def test_fail_find_command(self):
        # Evaluation
        found_command = self.persistence_implementation.find_command(self.non_existent_command_name)

        # Postconditions & Validations
        self.assertEqual(found_command, None)

    def test_delete_command(self):
        # Preconditions
        new_command = Command(self.command_name, self.command_path, self.command_date_of_creation)
        self.persistence_implementation.add_command(new_command)
        initial_length = len(self.persistence_implementation.list_commands())

        # Evaluation
        deleted = self.persistence_implementation.delete_command(self.command_name)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length - 1)
        self.assertTrue(deleted)

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
        new_command = Command(self.command_name, self.command_path, self.command_date_of_creation)
        self.persistence_implementation.add_command(new_command)
        initial_length = len(self.persistence_implementation.list_commands())

        # Evaluation
        updated = self.persistence_implementation.update_command(self.command_name, self.udpated_path)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length)
        self.assertTrue(updated)

    def test_fail_update_command(self):
        # Preconditions
        initial_length = len(self.persistence_implementation.list_commands())

        # Evaluation
        updated = self.persistence_implementation.update_command(self.non_existent_command_name, self.udpated_path)

        # Postconditions & Validations
        final_length = len(self.persistence_implementation.list_commands())
        self.assertEqual(final_length, initial_length)
        self.assertFalse(updated)


if __name__ == '__main__':
    unittest.main()
