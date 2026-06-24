"""
The `folder_methods` module provides a `Folder` class for creating, changing,  
deleting, and renaming directories with feedback displayed in a GUI window.
"""

import os

from ui.my_gui import Ui_MainWindow
from utils.utilities import Util


class Folder:
    """This 'folder' class provides methods to change directory, create directory,
    delete directory, and rename directory in Python."""

    def change(self, dir_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Attempts to change the current working directory to the specified directory.
        Args:
            dir_name (str): The name of the directory to change to.
            window (Ui_MainWindow): A reference to a GUI window object to display feedback.
        Returns:
            None
        """
        try:
            os.chdir(dir_name)

            message = "Directory changed successfully."
            cwd = f"Dir: {os.getcwd()}"  # update current dir
            window.plainTextEdit.setPlainText(message)
            window.plainTextEdit.setPlainText(cwd)

            # * update current dir
            current_dir = os.getcwd().upper()  # get current work dir
            window.currentDirLabel.setText(f"Current directory: {current_dir}")

        except NotADirectoryError:
            message = f"Error: '{dir_name}' is not a directory."
        except PermissionError:
            message = f"Error: permission denied for '{dir_name}'."
        except Exception as e:
            message = f"Unexpected error while changing directory: {e}"

        window.plainTextEdit.setPlainText(message)

    def create(self, dir_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Attempts to create a new directory.
        Args:
            dir_name (str): The name of the directory to create.
            window (Ui_MainWindow): A reference to a GUI window object to display feedback.
        Returns:
            None
        """
        try:
            os.makedirs(dir_name)  # this creates a directory on the current folder
            message = f"Directory {dir_name} created successfully."

        except FileExistsError:
            message = f"Error: directory '{dir_name}' already exists."
        except PermissionError:
            message = f"Error: permission denied to create '{dir_name}'."
        except Exception as e:
            message = f"Error creating directory '{dir_name}': {e}"

        window.plainTextEdit.setPlainText(message)

    def delete(self, dir_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Attempts to delete a directory.
        Args:
            dir_name (str): The name of the directory to delete.
            window (Ui_MainWindow): A reference to a GUI window object to display feedback.
        Returns:
            None
        """
        try:
            os.rmdir(dir_name)
            message = f"Directory {dir_name} deleted successfully."

        except FileNotFoundError:
            message = f"Error: directory '{dir_name}' not found."
        except OSError as e:
            message = f"Error deleting directory '{dir_name}': {e}"
        except Exception as e:
            message = f"Unexpected error while deleting '{dir_name}': {e}"

        window.plainTextEdit.setPlainText(message)

    def rename(
        self, dir_name: str, new_name: str, ok: bool, window: Ui_MainWindow
    ) -> None:
        """
        Summary:
            Attempts to rename a directory.
        Args:
            dir_name (str): The current name of the directory.
            new_name (str): The new name for the directory.
            ok (bool): A flag indicating whether to proceed with the rename operation.
            window (Ui_MainWindow): A reference to a GUI window object to display feedback.
        Returns:
            None
        """
        try:
            if ok:
                # Rename the directory
                os.rename(dir_name, new_name)
                message = f"Directory {dir_name} renamed to {new_name} successfully."
            else:
                message = "Rename operation cancelled."

        except FileNotFoundError:
            message = f"Error: directory '{dir_name}' not found."
        except FileExistsError:
            message = f"Error: target name '{new_name}' already exists. Choose another name to rename the directory."
        except PermissionError:
            message = f"Error: permission denied to rename '{dir_name}'."
        except Exception as e:
            message = f"Unexpected error while renaming '{dir_name}': {e}"

        window.plainTextEdit.setPlainText(message)

    def size(self, dir_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Calculates the size of a directory.
        Args:
            dir_name (str): The name of the directory.
            window (Ui_MainWindow): A reference to a GUI window object to display feedback.
        Returns:
            None
        """
        try:
            size = os.path.getsize(dir_name)
            message = f"Directory size: {size / 1024:.2f} kb"

        except NotADirectoryError:
            message = f"Error: '{dir_name}' is not a directory."
        except FileNotFoundError:
            message = f"Error: directory '{dir_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to access '{dir_name}'."
        except Exception as e:
            message = f"Error calculating size of '{dir_name}': {e}"

        window.plainTextEdit.setPlainText(message)
