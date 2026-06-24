"""
The `utilities` module provides a `Util` class for listing files, help and about message 
with feedback displayed in a GUI window.
"""

from os import getcwd
from pathlib import Path

from ui.my_gui import Ui_MainWindow

MESSAGE = """
File: mkfile, create, read, write, rewrite, delete, rename, size
Directory: mkdir, deletedir, renamedir, dirsize
Other: change, list, help

### The program supports the following commands:

-   mk: Create a new file -> Ex: mk file.py
-   read: Read the contents of a file -> Ex: read filename
-   write: Write to a file -> Ex: write filename text
-   rewrite: Rewrite the contents of a file -> Ex: rewrite filename text
-   delete: Delete a file -> Ex: delete filename
-   rename: Rename a file -> Ex: rename filename, then a box will appear to insert the new name
-   size: Display the size of a file -> Ex: size filename
-   mkdir: Create a new directory -> Ex: mkdir dirname
-   deletedir: Delete a directory -> Ex: deletedir dirname
-   renamedir: Rename a directory -> Ex: renamedir dirname, then a box will appear to insert the new name
-   dirsize: Display the size of a directory -> Ex: dirsize dirname
-   change: Change the current directory -> Ex: change dirname
-   list: List the files in the current directory -> Ex: list
-   help: Display help information -> Ex: help
-   about: Display information about the program -> Ex: about
-   clear: clear command-line interface -> Ex: clear"""

class Util:
    """
    A utility class for displaying file system information and providing help messages in a GUI window.
    """

    def current_dir(self, window: Ui_MainWindow) -> None:
        """
        Summary:
            Display the current working directory in a GUI window.
        Args:
            window (Ui_MainWindow): The GUI window to display the current directory.
        """
        current_dir = Path(getcwd()).resolve().as_posix().upper()
        window.currentDirLabel.setText(f"Current directory: {current_dir}")

    def list_files(self, window: Ui_MainWindow) -> None:
        """
        Summary:
            List all files and folders in the current working directory.
        Args:
            window (Ui_MainWindow): The GUI window to display the list of files.
        """
        current_dir = Path(getcwd()).resolve()
        list_files = sorted([f.name for f in current_dir.iterdir()])
        window.plainTextEdit.setPlainText("\n".join(list_files))

    def helper(self, window: Ui_MainWindow) -> None:
        """
        Summary:
            Display a help message with available commands.
        Args:
            window (Ui_MainWindow): The GUI window to display the help message.
        """

        window.plainTextEdit.setPlainText(MESSAGE)

    def about(self, window: Ui_MainWindow) -> None:
        """
        Summary:
            Display an about message with a brief description of the file system.
        Args:
            window (Ui_MainWindow): The GUI window to display the about message.
        """
        message = "This is a simple file system. It allows you to create, read, write"
        window.plainTextEdit.setPlainText(message)

    def clear(self, window: Ui_MainWindow) -> None:
        """
        Summary:
            Clear the text widget.
        Args:
            window (Ui_MainWindow): The GUI window with the text widget to clear.
        """
        window.plainTextEdit.clear()
