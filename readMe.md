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

### Micro Management of First Task
- Fully Implement the Configuration Manager
- Extends its usage to the persistence manager
- Minimize decoupling between implementations and configurations, should implementations have a link to the config file or should they not?
- Implement and revise the reset_implementation [JSON, YAML, SQLITE]

### What am i to do? Macro Management
- Finish shift_implementation() [Persitence Manager]
- Create persistence section of run_tests.py
- Create crud_tests
- Create crud section of run_tests.py
- Use the Tests!

- Create uninstall_commander.py, should be quite easy with reset_implementation
- list_local_commands
- get_current_configuration
- Improve interace contarct, return types and etc, whats the best value to return in each situation False? None?, is there a way to type the language kind of like a TypeScript
- Persistence Manager and Configuration Manager should be singletons

### Random
- Somehow use enum or constants for global variables, is there a way to define a constant based on the value property of a json, the script basically is guessing that in config there is a property called persistence
- Improve on visibility for the objects, usage of the interface is not as clean as in Java