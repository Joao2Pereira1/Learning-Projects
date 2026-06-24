from typing import Callable, Dict, List

from utils.file_methods import File  # Methods for file handling
from utils.folder_methods import Folder  # Methods for folder handling
from utils.utilities import Util  # Extra methods ex: about, help, list

# < commands
# Each key  represents a command that the user can input, and the
# corresponding value is the function that should be executed when command is entered.
COMMANDS: Dict[str, Callable] = {
    "mk": File.create,
    "read": File.read,
    "write": File.write,
    "rewrite": File.rewrite,
    "delete": File.delete,
    "rename": File.rename,
    "size": File.size,
    "mkdir": Folder.create,
    "deletedir": Folder.delete,
    "renamedir": Folder.rename,
    "dirsize": Folder.size,
    "change": Folder.change,
    "list": Util.list_files,
    "help": Util.helper,
    "about": Util.about,
    "clear": Util.clear,
}