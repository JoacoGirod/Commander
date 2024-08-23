import json

class Command:
    def __init__(self, command_name, path_to_bash_script, creation_date):
        self.command_name = command_name
        self.path_to_bash_script = path_to_bash_script
        self.creation_date = creation_date

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_data = json.loads(json_str)
        return cls(**json_data)

    def get_instance_as_dictionary(self):
        return self.__dict__

    def __str__(self):
        return f"<Command name='{self.command_name}', Python Script Path ='{self.path_to_python_or_bash_script}', Bash Script Path='{self.path_to_bash_script}' , date='{self.creation_date}'>"
