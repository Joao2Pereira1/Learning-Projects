"""
The `file_methods` module provides a `File` class for creating, reading, writing, 
deleting, renaming, and getting the size of files, with feedback displayed in a GUI window.
"""

import os

from ui.my_gui import \
    Ui_MainWindow  # Import the Ui_MainWindow class from PyQt5

# < file methods


class File:
    """The `file` class in Python provides methods for creating, reading, writing, deleting,
    renaming, and getting the size of files, with feedback displayed in a GUI window."""

    def create(self, file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            The function attempts to create a new file and provides feedback
            on the success or failure of the operation.
        Args:
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

        window.plainTextEdit.setPlainText(message)

    def read(self, file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            The function reads the contents of a file and displays a message indicating
            whether the file was read successfully or if an error occurred.
        Args:
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                message = f"Text on file: {file.read()}"
                message = f"File {file_name} read successfully."

        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to read '{file_name}'."
        except UnicodeDecodeError:
            message = f"Error: file '{file_name}' is not a valid UTF-8 text file."
        except Exception as e:
            message = f"Unexpected error reading '{file_name}': {e}"

        window.plainTextEdit.setPlainText(message)

    def rewrite(
        self, file_name: str, text: str, ok: bool, window: Ui_MainWindow
    ) -> None:
        """
        Summary:
            The function `rewrite` writes the given text to a file specified by `self`
            and displays a success message in a plain text edit window.
        Args:
          text: The `text` parameter in the `rewrite` function is the content that
            you want to write to the file specified by the `self` parameter. It is the
            text that will be written to the file.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        try:
            if ok:
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(text)

                message = f"File {file_name}: content changed successfully."
            else:
                print("Operation cancelled!")
        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to write to '{file_name}'."
        except Exception as e:
            message = f"Unexpected error rewriting '{file_name}': {e}"

        window.plainTextEdit.setPlainText(message)

    def write(self, file_name: str, text: str, ok: bool, window: Ui_MainWindow) -> None:
        """
        Summary:
            This function writes text to a file and displays a message in a window
            indicating whether the operation was successful or not.
        Args:
          text: The `text` parameter in the `write` method is the content that you
            want to write to the file. It is the text that will be appended to the file
            specified by the`self` parameter.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """
        try:
            if ok:
                with open(file_name, "a", encoding="utf-8") as file:
                    file.write(text)

                message = f"File {file_name}: content add successfully."
            else:
                print("Operation cancelled!")
        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to write to '{file_name}'."
        except Exception as e:
            message = f"Unexpected error writing to '{file_name}': {e}"

        window.plainTextEdit.setPlainText(message)

    def delete(self, file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            The function attempts to delete a file and displays a message indicating
            whether the deletion was successful or not.
        Args:
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


        window.plainTextEdit.setPlainText(message)

    def rename(self, file_name: str, new_name: str, ok: bool,window: Ui_MainWindow) -> None:
        """
        Summary:
            The function attempts to rename a file and displays a success message
            or an error message accordingly.
        Args:
          new_name (str): The new name for the file.
          window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """

        try:
            if ok:
                os.renames(file_name, new_name)
                message = f"File {file_name} renamed successfully."
            else:
                message = f"Renaming file to {file_name} wasn't possible."
        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except FileExistsError:
            message = f"Error: a file named '{new_name}' already exists."
        except PermissionError:
            message = f"Error: permission denied to rename '{file_name}'."
        except Exception as e:
            message = f"Unexpected error renaming '{file_name}': {e}"
        window.plainTextEdit.setPlainText(message)

    def size(self, file_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            The function retrieves the size of a file and displays it in kilobytes,
            handling errors if the file is not found.
        Args:
            window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
        """

        try:
            size = os.path.getsize(file_name)
            message = f"File size: {size} kb"

        except FileNotFoundError:
            message = f"Error: file '{file_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to access '{file_name}'."
        except IsADirectoryError:
            message = f"Error: '{file_name}' is a directory, not a file."
        except Exception as e:
            message = f"Unexpected error getting size of '{file_name}': {e}"

        window.plainTextEdit.setPlainText(message)
