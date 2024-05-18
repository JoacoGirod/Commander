# Commander
A group of python scripts that facilitate the creation of bash commands that can directly be executed through the terminal, the implementation is only prepared to execute a python script when the command is activated in the terminal.

### How to Install
```bash
    git clone https://github.com/JoacoGirod/commander
```
```bash
    cd commander
```
```bash
    sudo python3 install_commander.py
```

### Basic Functionalities
- Adds a new command to your local bash commands that will execute the python script in ```<path_to_script>```  when ```<command_name>``` is used in the bash terminal.
```bash
    sudo add_command <command_name> <path_to_script>
```
- If the command is found it retrieves the basic information from it.
```bash
    find_command <command_name>
```
- Lists all commands created through these scripts, '-a' will also retrieve all information available for the commands.
```bash
    list_commands [-a]
```
- Lists all commands in the local bash
```bash
    list_local_commands
```
- Shows the current Commander configuration
```bash
    get_configuration
```
- Updates ```<command_name>```'s python script to the one located in ```<new_path_to_script>```
```bash
    sudo update_command <command_name> <new_path_to_script>
```
- Deletes ```<command_name>``` from local bash if it exists
```bash
    sudo delete_command <command_name>
```
- Deletes the configuration, bash scripts and the persisted information, python scripts will continue to exist
```bash
    sudo erase_all_commands
```

### Main Usage Example
Assuming we have already installed Commander, we can create in /home/jgirod/Desktop/ the following script
```python
    # test_sum_args.py
    import sys

    def main():
        total = 0
        # Convert command-line arguments to integers and sum them up
        for arg in sys.argv[1:]:
            try:
                total += int(arg)
            except ValueError:
                print(f"Invalid argument: {arg}. Please provide integer arguments only.")

        print(f"Total sum: {total}")

    if __name__ == "__main__":
        main()
```
Then we could simply open a terminal and run
```bash
    sudo add_command sum_arguments /home/jgirod/Desktop/test_sum_args.py
```
And later use it whenever we find it necesarry by doing
```bash
    sum_arguments 45 54 34 1
```
