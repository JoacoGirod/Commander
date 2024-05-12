### Next Steps
- Create delete_command
- Create find_command
- Create installing script
- Create some basic tests, this should test the flexibility of the application as well, end to end should be idempotent, how can i make unit testing idempotent
- Revise code quality

### Pending
- ""config.json"" vs "../config.json", i guess it only matters during the installment (?)
- Somehow use enum or constants for global variables, is there a way to define a constant based on the value property of a json, the script basically is guessing that in config there is a property called persistence
- The Persistence Implementation should be interchangeable using the configuration script
- Create a second persistence implementation, some kind of lightweight sql db, like HyperSQL just to test the flexibility of the application. &YAML or other formats could also be fun
- Improve on visibility for the objects, usage of the interface is not as clean as in Java

### More Commands?
- Check Synchronization command for checking how the persistence matches with the /usr/local/bin
- List commands in the /usr/local/bin
- Delete All custom commands
- Uninstalling script?

### Commands for quick use
 Being in root folder
```
sudo python3 crud/add_commands.py test_command <path>
```
```
sudo python3 crud/list_commands.py [-a]
```


#### Installer
1. Ask for configuration values and write the JSON
2. Install the add_command
3. Use add_command to add the other main commands
4. Should somehow add to the history the add_command which would be omitted