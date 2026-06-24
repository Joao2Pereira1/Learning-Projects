"""
My Command-Line Interface App main module.

Author: João Pereira
"""

import sys

from controller.main_window_controller import MainWindowController
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

# Constants
STYLE_SHEET_FILE_PATH = "./app/styles/styles.qss"
ICON_FILE_PATH = "./icons/lighting.jpg"
WINDOW_OPACITY = 0.95


def load_style_sheet():
    """Load the stylesheet from file."""

    try:
        with open(STYLE_SHEET_FILE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        print(f"Error: Could not load stylesheet. {e}")
        return ""


def create_window():
    """Create the main window and set its properties."""

    window = MainWindowController()
    window.setWindowTitle("Lighting Terminal")
    window.setWindowIcon(QIcon(ICON_FILE_PATH))
    window.setWindowOpacity(WINDOW_OPACITY)
    return window


def run_application():
    """Run the application event loop."""

    app = QApplication(sys.argv)
    style_sheet = load_style_sheet()
    app.setStyleSheet(style_sheet)

    window = create_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_application()
