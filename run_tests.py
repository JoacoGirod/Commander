import unittest
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from persistence.PersistenceManager import *
from configuration.ConfigurationManager import *

class TestPersistenceImplementations(unittest.TestCase):

    def setUp(self):
        subprocess.run(["python3", "install_commander.py"], check=True)
        self.persistenceManager = PersistenceManager()

    def tearDown(self):
        PersistenceManager().get_implementation().reset_implementation()
        ConfigurationManager().delete_configuration()

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

if __name__ == '__main__':
    unittest.main()
