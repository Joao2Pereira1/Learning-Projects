"""
My Todo List App main module.
"""

import logging
import sys

from controller.main_window_controller import MainWindowController
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

# * Constants
STYLE_SHEET_FILE = "./app/styles/styles.qss"
ICON_FILE = "./app/icons/lighting.jpg"
WINDOW_OPACITY = 0.95


def load_style_sheet() -> str:
    """
    Load the application's stylesheet from a file.

    Returns:
        str: The stylesheet as a string.
    """
    try:
        with open(STYLE_SHEET_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        logging.error(f"Error: Could not load stylesheet. {e}")
        return "Error"


def set_up_window_properties(window: MainWindowController) -> None:
    """
    Set up the properties of the main window.

    Args:
        window: The main window controller.
    """
    window.setWindowTitle("My Todo List App")
    window.setWindowIcon(QIcon(ICON_FILE))
    window.setWindowOpacity(WINDOW_OPACITY)


# < RUNNING


def main():
    """
    Entry point of the application. Starts the to do app
    """
    app = QApplication(sys.argv)

    # ? SET UP APPEARANCE FILE
    if load_style_sheet() == "Error":
        logging.error("Could not load stylesheet. Exiting...")
    else:
        app.setStyleSheet(load_style_sheet())

    window = MainWindowController()

    set_up_window_properties(window)  # window properties

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
