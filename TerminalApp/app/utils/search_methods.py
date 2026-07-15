import os
from ui.my_gui import Ui_MainWindow  # Import the Ui_MainWindow class from PyQt5


def find_files(directory: str, filename_to_find: str, window: Ui_MainWindow) -> None:
    """
    Summary:
        The function searches for files containing the given search term by recursively
        scanning the current directory and all of its subdirectories.
    Args:
        window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
    """
    results = []
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if filename_to_find.lower() in file.lower():
                    relative_path = os.path.relpath(os.path.join(root, file), directory)
                    results.append(relative_path)

        if not results:
            message = f"No files found containing the name: '{filename_to_find}'"
        else:
            message = "\n".join(results)

    except PermissionError:
        message = f"Error: permission denied to scan the directory '{directory}'."
    except Exception as e:
        message = f"Unexpected error during search: {e}"

    window.plainTextEdit.setPlainText(message)


def grep_text(
    directory: str, file_name: str, text_to_find: str, window: Ui_MainWindow
) -> None:
    """
    Summary:
        The function reads a specific file line by line to search for a given text match,
        returning the matching lines along with their respective line numbers.
    Args:
        window: its a reference to a GUI window object and the method being used
            will display a informative message to user into a text widget
    """
    file_path = os.path.join(directory, file_name)

    if not os.path.exists(file_path):
        message = (
            f"Error: the file '{file_name}' does not exist in the current directory."
        )
        window.plainTextEdit.setPlainText(message)
        return

    if os.path.isdir(file_path):
        message = f"Error: '{file_name}' is a directory, not a file."
        window.plainTextEdit.setPlainText(message)
        return

    results = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line_num, line in enumerate(file, 1):
                if text_to_find.lower() in line.lower():
                    results.append(f"Line {line_num}: {line.strip()}")

        if not results:
            message = f"No matches found for '{text_to_find}' inside '{file_name}'."
        else:
            message = "\n".join(results)

    except PermissionError:
        message = f"Error: permission denied to read '{file_name}'."
    except Exception as e:
        message = f"Unexpected error reading '{file_name}': {e}"

    window.plainTextEdit.setPlainText(message)
