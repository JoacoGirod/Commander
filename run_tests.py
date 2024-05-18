import unittest
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from pathlib import Path
from persistence.PersistenceManager import *
from configuration.ConfigurationManager import *

class TestPersistenceImplementations(unittest.TestCase):

    def setUp(self):
        if Path("config.json").exists():
            print("\nTHE APPLICATION HAS ALREADY BEEN INSTALLED, RUNNING THE TESTS WOULD ERASE THE CURRENT SESSION\n")
            sys.exit(0)
        subprocess.run(["python3", "install_commander.py"], check=True)
        self.persistenceManager = PersistenceManager()

    def test_persistence_implementations(self):
        # JSON
        print("|||--JSON--|||")
        json_impl = self.persistenceManager.get_implementation()
        json_impl.reset_implementation()
        subprocess.run(["python3", "tests/persistence_tests/persistence_implementation_test.py"], check=True)
        # YAML
        print("|||--YAML--|||")
        self.persistenceManager.shift_implementation(PersistenceImplementation.YAML.value)
        yaml_impl = self.persistenceManager.get_implementation()
        yaml_impl.reset_implementation()
        subprocess.run(["python3", "tests/persistence_tests/persistence_implementation_test.py"], check=True)
        # SQLite
        print("|||--SQLite--|||")
        self.persistenceManager.shift_implementation(PersistenceImplementation.SQLITE.value)
        sqlite_impl = self.persistenceManager.get_implementation()
        sqlite_impl.reset_implementation()
        subprocess.run(["python3", "tests/persistence_tests/persistence_implementation_test.py"], check=True)

        PersistenceManager().get_implementation().reset_implementation()
        ConfigurationManager().delete_configuration()

    def test_crud(self):
        subprocess.run(["python3", "install_commander.py"], check=True)
        subprocess.run(["python3", "tests/crud_tests/crud_test.py"], check=True)
        # erase_all_commands already

if __name__ == '__main__':
    unittest.main()
