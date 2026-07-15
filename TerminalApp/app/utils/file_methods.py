"""
The `file_methods` module provides a `File` class for creating, reading, writing,
deleting, renaming, and getting the size of files, with feedback displayed in a GUI window.
"""

import os

from ui.my_gui import Ui_MainWindow  # Import the Ui_MainWindow class from PyQt5

# < file methods


class File:
    """The `File` class provides static methods for creating, reading, writing,
    deleting, renaming, and getting the size of files, with feedback displayed
    in a GUI window."""

    def create(file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            The function attempts to create a new file and provides feedback
            on the success or failure of the operation.
        Args:
          file_name (str): The name of the file to create.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        try:
            with open(file_name, "x", encoding="utf-8") as file:
                file.write("")

            message = f"File {file_name} created successfully."

        except FileExistsError:
            message = f"Error: file '{file_name}' already exists."
        except PermissionError:
            message = f"Error: permission denied to create '{file_name}'."
        except Exception as e:
            message = f"Unexpected error creating '{file_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def read(file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Reads the contents of a file and displays them in the terminal
            output, or an error message if the file could not be read.
        Args:
          file_name (str): The name of the file to read.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
            message = (
                f"--- {file_name} ---\n{content}"
                if content
                else f"File '{file_name}' is empty."
            )

        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to read '{file_name}'."
        except IsADirectoryError:
            message = f"Error: '{file_name}' is a directory, not a file."
        except UnicodeDecodeError:
            message = f"Error: file '{file_name}' is not a valid UTF-8 text file."
        except Exception as e:
            message = f"Unexpected error reading '{file_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def rewrite(file_name: str, text: str, ok: bool, window: Ui_MainWindow) -> None:
        """
        Summary:
            Overwrites the contents of a file with the given text.
        Args:
          file_name (str): The file to overwrite.
          text (str): The new content of the file.
          ok (bool): Whether the user confirmed the input dialog.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        if not ok:
            window.plainTextEdit.appendPlainText("Operation cancelled.")
            return

        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(text)

            message = f"File {file_name}: content changed successfully."
        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to write to '{file_name}'."
        except IsADirectoryError:
            message = f"Error: '{file_name}' is a directory, not a file."
        except Exception as e:
            message = f"Unexpected error rewriting '{file_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def write(file_name: str, text: str, ok: bool, window: Ui_MainWindow) -> None:
        """
        Summary:
            Appends the given text to the end of a file.
        Args:
          file_name (str): The file to append to.
          text (str): The content to append to the file.
          ok (bool): Whether the user confirmed the input dialog.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        if not ok:
            window.plainTextEdit.appendPlainText("Operation cancelled.")
            return

        try:
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(text)

            message = f"File {file_name}: content added successfully."
        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to write to '{file_name}'."
        except IsADirectoryError:
            message = f"Error: '{file_name}' is a directory, not a file."
        except Exception as e:
            message = f"Unexpected error writing to '{file_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def delete(file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Attempts to delete a file and displays a message indicating
            whether the deletion was successful or not.
        Args:
          file_name (str): The file to delete.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        try:
            os.remove(file_name)
            message = f"File {file_name} deleted successfully."

        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to delete '{file_name}'."
        except IsADirectoryError:
            message = f"Error: '{file_name}' is a directory, not a file."
        except Exception as e:
            message = f"Unexpected error deleting '{file_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def rename(file_name: str, new_name: str, ok: bool, window: Ui_MainWindow) -> None:
        """
        Summary:
            Attempts to rename a file and displays a success message
            or an error message accordingly.
        Args:
          file_name (str): The current name of the file.
          new_name (str): The new name for the file.
          ok (bool): Whether the user confirmed the input dialog.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        if not ok:
            window.plainTextEdit.appendPlainText("Rename operation cancelled.")
            return

        try:
            os.rename(file_name, new_name)
            message = f"File {file_name} renamed to {new_name} successfully."
        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except FileExistsError:
            message = f"Error: a file named '{new_name}' already exists."
        except PermissionError:
            message = f"Error: permission denied to rename '{file_name}'."
        except Exception as e:
            message = f"Unexpected error renaming '{file_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def size(file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Retrieves the size of a file and displays it in a human-readable
            way, handling errors if the file is not found.
        Args:
            file_name (str): The file to inspect.
            window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        try:
            size_bytes = os.path.getsize(file_name)
            message = f"File size: {size_bytes} bytes ({size_bytes / 1024:.2f} KB)"

        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to access '{file_name}'."
        except IsADirectoryError:
            message = f"Error: '{file_name}' is a directory, not a file."
        except Exception as e:
            message = f"Unexpected error getting size of '{file_name}': {e}"

        window.plainTextEdit.appendPlainText(message)
