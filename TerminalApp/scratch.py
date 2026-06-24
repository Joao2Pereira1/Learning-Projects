# Program for files and directories functionalities like creating, renaming, deleting, etc

# todo first do with the terminal, then do with GUI use pyqt 6 use the design mode

from os import getcwd as getdir  # only using one method no need to import the whole

import utils.utilities as util
from utils.file_methods import file
from utils.folder_methods import folder

# < commands
# Each key  represents a command that the user can input, and the
# corresponding value is the function that should be executed when command is entered.
COMMANDS = {
    "mk": file.create,
    "read": file.read,
    "write": file.write,
    "rewrite": file.rewrite,
    "delete": file.delete,
    "rename": file.rename,
    "size": file.size,
    "mkdir": folder.create,
    "deletedir": folder.delete,
    "renamedir": folder.rename,
    "dirsize": folder.size,
    "change": folder.change,
    "list": util.list_files,
    "help": util.helper,
    "about": util.about,
}


# < main function
def main():
    """
    The main function takes user commands to interact with files and directories, providing options to
    create, read, write, rename, delete files and directories, change directories, list files, and
    display help information.

    Returns:
      The `main()` function is returning `False` when the command "exit" is entered, which will break
    out of the while loop and end the program.
    """

    while True:
        command = input("Enter command: ").lower().lstrip()
        print("Dir: " + getdir())  # update current dir

        if command == "exit":
            return False

        if command in COMMANDS:
            if command in [
                "mk",
                "read",
                "write",
                "rewrite",
                "type",
                "delete",
                "rename",
                "size",
            ]:  # file commands
                name = input("Enter the file name: ")
                COMMANDS[command](name)

            elif command in [
                "change",
                "mkdir",
                "deletedir",
                "renamedir",
                "dirsize",
            ]:  # directory commands
                name = input("Enter the directory name: ")
                COMMANDS[command](name)
            else:
                COMMANDS[command]()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
