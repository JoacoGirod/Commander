from abc import ABC, abstractmethod

class CommandPersistenceDao(ABC):

    @abstractmethod
    def add_command(new_command):
        pass

    @abstractmethod
    def list_commands():
        pass

    @abstractmethod
    def find_command():
        pass

    @abstractmethod
    def delete_command(command_to_delete):
        pass

    @abstractmethod
    def update_command(command_to_update):
        pass

    @abstractmethod
    def reset_implementation():
        pass