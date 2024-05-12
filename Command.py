import json

class Command:
    def __init__(self, command_name, path_to_script, creation_date):
        self.command_name = command_name
        self.path_to_script = path_to_script
        self.creation_date = creation_date

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_data = json.loads(json_str)
        return Command(**json_data)

    def __str__(self):
        return f"<Command name='{self.command_name}', path='{self.path_to_script}', date='{self.creation_date}'>"
