# Install
```
    git clone https://github.com/JoacoGirod/commander
```
```
    cd commander
```
```
    sudo python3 install_commander.py
```

# Basic Functionalities
- Adds a new command to your local bash, the command executes the python script specified
```
    sudo add_command <command_name> <path_to_script>
```
- If the command is found it retrieves the basic information from it
```
    sudo find_command <command_name>
```
- Lists all commands created through these scripts, '-a' will also retrieve all information available for the commands
```
    sudo list_commands [-a]
```
- Lists all commands in the local bash
```
    sudo list_local_commands
```
- Updates the command's script
```
    sudo update_command <command_name> <new_path_to_script>
```
- Deletes command from local bash
```
    sudo delete_command <command_name>
```

### When to stop
- list_local_commands
- Somehow use enum or constants for global variables, is there a way to define a constant based on the value property of a json, the script basically is guessing that in config there is a property called persistence
- Create a second persistence implementation, some kind of lightweight sql db, like HyperSQL just to test the flexibility of the application. YAML or other formats could also be fun
- Improve on visibility for the objects, usage of the interface is not as clean as in Java
- Configuration Command (?), changing persistence strategy should transfer the information
- Uninstall script(?)