"""
My Command-Line Interface App main module.

Author: João Pereira
"""

import sys

from pathlib import Path
from controller.main_window_controller import MainWindowController
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

# Base directory of the current script (app/ folder)
BASE_DIR = Path(__file__).resolve().parent

# Dynamic absolute paths using pathlib
STYLE_SHEET_FILE_PATH = BASE_DIR / "styles" / "styles.qss"
ICON_FILE_PATH = BASE_DIR / "resources" / "icons" / "flash.jpg"
WINDOW_OPACITY = 0.95


def load_style_sheet():
    """Load the stylesheet from file."""

    try:
        # pathlib allows reading text directly and safely with encoding
        if STYLE_SHEET_FILE_PATH.exists():
            return STYLE_SHEET_FILE_PATH.read_text(encoding="utf-8")
        else:
            print(f"Warning: Stylesheet file not found at {STYLE_SHEET_FILE_PATH}")
            return ""
    except IOError as e:
        print(f"Error: Could not load stylesheet. {e}")
        return ""


def create_window():
    """Create the main window and set its properties."""

    window = MainWindowController()
    window.setWindowTitle("Flash Terminal")
    window.setWindowIcon(QIcon(ICON_FILE_PATH.as_posix()))
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
