"""
The `utilities` module provides a `Util` class for listing files, managing
the help/about messages, and handling terminal utilities within a GUI window.
"""

from os import getcwd
from pathlib import Path
from ui.my_gui import Ui_MainWindow

MESSAGE = """======================================================================
                         AVAILABLE COMMANDS
======================================================================

File Commands:
  mk        - Create a new file               -> Ex: mk file.py
  read      - Read the contents of a file     -> Ex: read filename
  write     - Append text to a file           -> Ex: write filename text
  rewrite   - Rewrite the contents of a file   -> Ex: rewrite filename text
  delete    - Delete a file                   -> Ex: delete filename
  rename    - Rename a file                   -> Ex: rename filename
  size      - Display the size of a file       -> Ex: size filename

Directory Commands:
  mkdir     - Create a new directory          -> Ex: mkdir dirname
  deletedir - Delete a directory              -> Ex: deletedir dirname
  renamedir - Rename a directory              -> Ex: renamedir dirname
  dirsize   - Display the size of a directory  -> Ex: dirsize dirname
  change    - Change the current directory    -> Ex: change dirname

Search Commands:
  find      - Search for files by name        -> Ex: find .txt
  grep      - Search for text inside a file   -> Ex: grep file.txt "text"

Customization Commands:
  set color - Change terminal text color      -> Ex: set color #00ffcc
  set font  - Change terminal font size       -> Ex: set font 14

General Commands:
  list      - List all files in current dir   -> Ex: list
  clear     - Clear the terminal interface    -> Ex: clear
  help      - Display this help information   -> Ex: help
  about     - Display program information     -> Ex: about

======================================================================"""


class Util:
    """
    A utility class for displaying file system information and providing help messages in a GUI window.
    """

    def current_dir(window: Ui_MainWindow) -> None:
        """
        Summary:
            Display the current working directory in a GUI window.
        Args:
            window: its a reference to a GUI window object and the method being used
                will display a informative message to user into a text widget
        """
        current_dir = Path(getcwd()).resolve().as_posix().upper()
        window.currentDirLabel.setText(f"Current directory: {current_dir}")

    def list_files(window: Ui_MainWindow) -> None:
        """
        Summary:
            List all files and folders in the current working directory.
        Args:
            window: its a reference to a GUI window object and the method being used
                will display a informative message to user into a text widget
        """
        try:
            current_dir = Path(getcwd()).resolve()
            list_files = sorted([f.name for f in current_dir.iterdir()])

            if not list_files:
                message = "The directory is empty."
            else:
                message = "\n".join(list_files)

        except PermissionError:
            message = "Error: permission denied to list files in this directory."
        except Exception as e:
            message = f"Unexpected error listing files: {e}"

        window.plainTextEdit.setPlainText(message)

    def helper(window: Ui_MainWindow) -> None:
        """
        Summary:
            Display a help message with available commands.
        Args:
            window: its a reference to a GUI window object and the method being used
                will display a informative message to user into a text widget
        """
        window.plainTextEdit.setPlainText(MESSAGE)

    def about(window: Ui_MainWindow) -> None:
        """
        Summary:
            Display an about message with a brief description of the file system.
        Args:
            window: its a reference to a GUI window object and the method being used
                will display a informative message to user into a text widget
        """
        message = (
            "======================================================================\n"
            "                         ABOUT TERMINAL APP                           \n"
            "======================================================================\n\n"
            "This is a modern file system terminal simulator built with Python and PyQt5.\n"
            "It features a robust MVC architecture, strict exception handling, and\n"
            "comprehensive utilities to create, read, search, and manage files or directories.\n\n"
            "Developed as a high-quality portfolio project."
        )
        window.plainTextEdit.setPlainText(message)

    def clear(window: Ui_MainWindow) -> None:
        """
        Summary:
            Clear the text widget.
        Args:
            window: its a reference to a GUI window object and the method being used
                will display a informative message to user into a text widget
        """
        window.plainTextEdit.clear()
