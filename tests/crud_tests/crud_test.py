import unittest
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(PARENT_DIR)
sys.path.append(ROOT_DIR)

from pathlib import Path
from persistence.PersistenceManager import *
from configuration.ConfigurationManager import *
from crud.add_command import main as add_command
from crud.delete_command import main as delete_command
from crud.erase_all_commands import main as erase_all_commands
from crud.find_command import main as find_command
from crud.list_commands import main as list_commands
from crud.update_command import main as update_command

class TestCrud(unittest.TestCase):

    def setUp(self):
        subprocess.run(["python3", "install_commander.py"], check=True)
        self.persistenceManager = PersistenceManager()
        self.command_name = "test_command"
        self.non_existent_command_name = "non_existent_command_name"
        self.python_command_path = "/path/to/python/command"
        self.bash_command_path = "/path/to/bash/command"
        self.updated_python_path = "/path/to/updated/python/command"
        self.updated_bash_path = "/path/to/updated/bash/command"

    def tearDown(self):
        PersistenceManager().get_implementation().reset_implementation()
        ConfigurationManager().delete_configuration()

    # These could be much more exhausting and check the fail cases, currently it only check for exceptions in execution
    def test_end_to_end_crud(self):
        # list_commands
        completed_process = subprocess.run(["python3", "crud/list_commands.py"], capture_output=True, text=True)
        print("list_commands output:")
        print(completed_process.stdout)
        print("list_commands errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # get_current_configuration
        completed_process = subprocess.run(["python3", "crud/get_current_configuration.py"], capture_output=True, text=True)
        print("list_commands output:")
        print(completed_process.stdout)
        print("list_commands errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # list_local_commands
        completed_process = subprocess.run(["python3", "crud/list_local_commands.py"], capture_output=True, text=True)
        print("list_commands output:")
        print(completed_process.stdout)
        print("list_commands errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # add_command
        completed_process = subprocess.run(["python3", "crud/add_command.py", self.command_name, self.python_command_path], capture_output=True, text=True)
        print("add_command output:")
        print(completed_process.stdout)
        print("add_command errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # find_command
        completed_process = subprocess.run(["python3", "crud/find_command.py", self.command_name], capture_output=True, text=True)
        print("find_command output:")
        print(completed_process.stdout)
        print("find_command errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # update_command
        completed_process = subprocess.run(["python3", "crud/update_command.py", self.command_name, self.updated_python_path], capture_output=True, text=True)
        print("update_command output:")
        print(completed_process.stdout)
        print("update_command errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # find_command after update
        completed_process = subprocess.run(["python3", "crud/find_command.py", self.command_name], capture_output=True, text=True)
        print("find_command after update output:")
        print(completed_process.stdout)
        print("find_command after update errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # delete_command
        completed_process = subprocess.run(["python3", "crud/delete_command.py", self.command_name], capture_output=True, text=True)
        print("delete_command output:")
        print(completed_process.stdout)
        print("delete_command errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # find_command after delete
        completed_process = subprocess.run(["python3", "crud/find_command.py", self.command_name], capture_output=True, text=True)
        print("find_command after delete output:")
        print(completed_process.stdout)
        print("find_command after delete errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)

        # list_commands
        completed_process = subprocess.run(["python3", "crud/list_commands.py"], capture_output=True, text=True)
        print("list_commands output:")
        print(completed_process.stdout)
        print("list_commands errors:")
        print(completed_process.stderr)
        self.assertEqual(completed_process.returncode, 0)



if __name__ == '__main__':
    unittest.main()
