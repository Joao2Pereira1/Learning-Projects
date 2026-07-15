"""
The `folder_methods` module provides a `Folder` class for creating, changing,
deleting, and renaming directories with feedback displayed in a GUI window.
"""

import os

from ui.my_gui import Ui_MainWindow
from utils.utilities import Util


class Folder:
    """The `Folder` class provides static methods to change directory, create
    directory, delete directory, and rename directory."""

    def change(dir_name: str, window: Ui_MainWindow) -> None:
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
            message = f"Directory changed to: {os.getcwd()}"

            # * update current dir label
            current_dir = os.getcwd().upper()
            window.currentDirLabel.setText(f"Current directory: {current_dir}")

        except FileNotFoundError:
            message = f"Error: directory '{dir_name}' not found."
        except NotADirectoryError:
            message = f"Error: '{dir_name}' is not a directory."
        except PermissionError:
            message = f"Error: permission denied for '{dir_name}'."
        except Exception as e:
            message = f"Unexpected error while changing directory: {e}"

        window.plainTextEdit.appendPlainText(message)

    def create(dir_name: str, window: Ui_MainWindow) -> None:
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
            os.makedirs(dir_name)
            message = f"Directory {dir_name} created successfully."

        except FileExistsError:
            message = f"Error: directory '{dir_name}' already exists."
        except PermissionError:
            message = f"Error: permission denied to create '{dir_name}'."
        except Exception as e:
            message = f"Error creating directory '{dir_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def delete(dir_name: str, window: Ui_MainWindow) -> None:
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
            message = f"Error deleting directory '{dir_name}': {e} (must be empty)"
        except Exception as e:
            message = f"Unexpected error while deleting '{dir_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def rename(dir_name: str, new_name: str, ok: bool, window: Ui_MainWindow) -> None:
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
        if not ok:
            window.plainTextEdit.appendPlainText("Rename operation cancelled.")
            return

        try:
            os.rename(dir_name, new_name)
            message = f"Directory {dir_name} renamed to {new_name} successfully."
        except FileNotFoundError:
            message = f"Error: directory '{dir_name}' not found."
        except FileExistsError:
            message = f"Error: target name '{new_name}' already exists."
        except PermissionError:
            message = f"Error: permission denied to rename '{dir_name}'."
        except Exception as e:
            message = f"Unexpected error while renaming '{dir_name}': {e}"

        window.plainTextEdit.appendPlainText(message)

    def size(dir_name: str, window: Ui_MainWindow) -> None:
        """
        Summary:
            Recursively calculates the total size of all files inside a directory.
        Args:
            dir_name (str): The name of the directory.
            window (Ui_MainWindow): A reference to a GUI window object to display feedback.
        Returns:
            None
        """
        try:
            if not os.path.isdir(dir_name):
                raise NotADirectoryError

            total_size = 0
            file_count = 0
            for root, _dirs, files in os.walk(dir_name):
                for f in files:
                    file_path = os.path.join(root, f)
                    try:
                        total_size += os.path.getsize(file_path)
                        file_count += 1
                    except OSError:
                        continue  # skip broken symlinks / inaccessible files

            message = (
                f"Directory size: {total_size / 1024:.2f} KB " f"({file_count} file(s))"
            )

        except NotADirectoryError:
            message = f"Error: '{dir_name}' is not a directory."
        except FileNotFoundError:
            message = f"Error: directory '{dir_name}' not found."
        except PermissionError:
            message = f"Error: permission denied to access '{dir_name}'."
        except Exception as e:
            message = f"Error calculating size of '{dir_name}': {e}"

        window.plainTextEdit.appendPlainText(message)
