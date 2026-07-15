from os import getcwd  # only using one method no need to import the everything
from typing import List

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QKeyEvent
from ui.my_gui import Ui_MainWindow  # UI design for the application
from utils.commands import COMMANDS
from utils.utilities import Util  # Extra methods ex: about, help, list
from utils.settings_handler import load_settings, save_settings

# Commands that take no extra arguments beyond the command name itself.
NO_ARG_COMMANDS = ["list", "help", "clear", "about"]

# Commands that operate on a single file name: `cmd filename`.
FILE_COMMANDS = ["mk", "read", "delete", "size"]

# Commands that operate on a single directory name: `cmd dirname`.
DIR_COMMANDS = ["change", "mkdir", "deletedir", "dirsize"]

PROMPT = ">"


class MainWindowController(QMainWindow):

    def __init__(self) -> None:
        """
        self → the main window (QMainWindow) that will be displayed on the screen.

        Ui_MainWindow → the interface class created in Qt Designer.

        self.ui.setupUi(self) → method of the Ui_MainWindow class
        that takes a window (QMainWindow) as an argument and is responsible
        for adding the widgets created in Qt Designer
        into the main window (self).
        """
        super().__init__()  # inherits QMainWindow
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        # 1. Loads previous session configs from JSON file
        saved_data = load_settings()

        # 2. Assign configuration values to terminal state variables
        self._terminal_background: str = saved_data["background"]
        self._terminal_foreground: str = saved_data["foreground"]
        self._terminal_font_size: int = saved_data["font_size"]

        # 3. Restore command history from persistent storage
        self._history: List[str] = saved_data["history"]
        self._history_index: int = len(self._history)
        self._current_input_cache: str = ""

        # 4. Create the Menu Bar on top dynamically
        self._create_menu_bar()

        # 5. Overwrite the default styles right away using the loaded parameters
        self._apply_dynamic_style()

        # * Event handlers

        # display
        Util.current_dir(self.ui)  # display current dir

        # autocomplete for command names
        completer = QCompleter(sorted(COMMANDS.keys()), self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit.setCompleter(completer)

        # buttons
        self.ui.pushButton.clicked.connect(self.handle_input)  # clicking button
        self.ui.lineEdit.returnPressed.connect(self.handle_input)  # Enter key
        self.ui.lineEdit.installEventFilter(self)  # catch Up/Down for history

        self.ui.plainTextEdit.appendPlainText(
            "Welcome! Type 'help' to see the list of available commands.\n"
        )

    def eventFilter(self, source, event):
        """Intercepts Up/Down key presses on the input line to navigate
        through the command history, like a regular shell."""
        if source is self.ui.lineEdit and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Up:
                self._navigate_history(-1)
                return True
            if event.key() == Qt.Key_Down:
                self._navigate_history(1)
                return True
        return super().eventFilter(source, event)

    def _navigate_history(self, step: int) -> None:
        """Moves the history cursor by `step` and updates the input line."""
        if not self._history:
            return

        if self._history_index == len(self._history) and step == -1:
            self._current_input_cache = self.ui.lineEdit.text()

        new_index = self._history_index + step

        if new_index < 0:
            new_index = 0
        elif new_index >= len(self._history):
            new_index = len(self._history)
            self.ui.lineEdit.setText(self._current_input_cache)
            self._history_index = new_index
            return

        self._history_index = new_index
        self.ui.lineEdit.setText(self._history[self._history_index])

    def _echo(self, raw_input: str) -> None:
        """Prints the command the user typed, terminal-style, before its output."""
        self.ui.plainTextEdit.appendPlainText(f"{PROMPT} {raw_input}")

    def _apply_dynamic_style(self) -> None:
        """
        Summary:
            Applies customization rules to the terminal widgets and window background,
            forcing an instant visual refresh and saving the state to the JSON file.
        Args:
            None
        """
        # Style applied to the window background to follow the theme
        self.setStyleSheet(
            f"QMainWindow {{ background-color: {self._terminal_background}; }}"
        )

        # Specific style for the Output Area
        output_style = f"""
            QPlainTextEdit {{
                background-color: {self._terminal_background};
                color: {self._terminal_foreground};
                font-family: "Consolas", "Fira Code", "Courier New", monospace;
                font-size: {self._terminal_font_size}px;
                border: 2px solid #2a2a30;
                border-radius: 8px;
                padding: 10px;
            }}
            QPlainTextEdit::selection {{
                background-color: {self._terminal_foreground};
                color: {self._terminal_background};
            }}
        """

        # Specific style for the Input Line
        input_style = f"""
            QLineEdit {{
                background-color: #1a1a1e;
                color: {self._terminal_foreground};
                font-family: "Consolas", "Fira Code", monospace;
                font-size: {self._terminal_font_size}px;
                border: 2px solid #2a2a30;
                border-radius: 6px;
                padding: 8px;
            }}
            QLineEdit:focus {{
                border: 2px solid {self._terminal_foreground};
            }}
        """

        # Apply localized stylesheets (forces overwrite without stacking memory)
        self.ui.plainTextEdit.setStyleSheet(output_style)
        self.ui.lineEdit.setStyleSheet(input_style)

        # Force Qt to completely repaint the widgets with the new attributes
        for widget in [self.ui.plainTextEdit, self.ui.lineEdit, self]:
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()

        # Save the updated state to the target absolute path in the 'data' directory
        save_settings(
            self._terminal_background,
            self._terminal_foreground,
            self._terminal_font_size,
            self._history,
        )

    def _create_menu_bar(self) -> None:
        """Creates a modern menu bar at the top for quick customization."""
        menu_bar = self.menuBar()

        # Themes (Matrix,White,Dracula)
        theme_menu = menu_bar.addMenu("Themes")
        matrix_action = theme_menu.addAction("Matrix Green")
        matrix_action.triggered.connect(lambda: self._set_theme("#121214", "#00ffcc"))
        classic_action = theme_menu.addAction("Classic White")
        classic_action.triggered.connect(lambda: self._set_theme("#ffffff", "#4F4F4F"))
        dracula_action = theme_menu.addAction("Dracula Purple")
        dracula_action.triggered.connect(lambda: self._set_theme("#282a36", "#ff79c6"))

        font_menu = menu_bar.addMenu("Font Size")
        small_action = font_menu.addAction("Small (11px)")
        small_action.triggered.connect(lambda: self._set_font_size(11))
        normal_action = font_menu.addAction("Normal (13px)")
        normal_action.triggered.connect(lambda: self._set_font_size(13))
        large_action = font_menu.addAction("Large (18px)")
        large_action.triggered.connect(lambda: self._set_font_size(18))

    def _set_theme(self, bg: str, fg: str) -> None:
        self._terminal_background = bg
        self._terminal_foreground = fg
        self._apply_dynamic_style()

    def _set_font_size(self, size: int) -> None:
        self._terminal_font_size = size
        self._apply_dynamic_style()

    def handle_input(self) -> int:
        """Handles the user input and executes the corresponding command."""
        raw_input = self.ui.lineEdit.text()
        command: List[str] = raw_input.split()  # get arguments
        num_args: int = len(command)

        self.ui.lineEdit.setText("")  # clear text

        if num_args == 0:
            return 0  # ignore empty submissions silently, like a real shell

        # Record in history (avoid consecutive duplicates) and echo the input
        if not self._history or self._history[-1] != raw_input:
            self._history.append(raw_input)

            # Save historical commands immediately to JSON
            save_settings(
                self._terminal_background,
                self._terminal_foreground,
                self._terminal_font_size,
                self._history,
            )

        self._history_index = len(self._history)
        self._current_input_cache = ""
        self._echo(raw_input)

        command = [command[0].lower(), *command[1:]]
        cmd: str = command[0]

        if cmd not in COMMANDS and cmd != "set":
            self.ui.plainTextEdit.appendPlainText(
                f"Invalid command: '{cmd}'. Type 'help' to see available commands."
            )
            Util.current_dir(self.ui)
            return 0

        if num_args == 1 and cmd in NO_ARG_COMMANDS:
            COMMANDS[cmd](self.ui)
        elif cmd in FILE_COMMANDS:
            file_name: str = " ".join(command[1:])
            if file_name:
                COMMANDS[cmd](file_name, self.ui)
            else:
                self.ui.plainTextEdit.appendPlainText("Invalid file name.")
        elif cmd in DIR_COMMANDS:
            dir_name: str = " ".join(command[1:])
            if dir_name:
                COMMANDS[cmd](dir_name, self.ui)
            else:
                self.ui.plainTextEdit.appendPlainText("Invalid directory name.")
        elif cmd == "find":
            if num_args < 2:
                self.ui.plainTextEdit.appendPlainText("Correct usage: find [filename]")
            else:
                search_term = " ".join(command[1:])
                COMMANDS[cmd](search_term, self.ui)
        elif cmd == "grep":
            if num_args < 3:
                self.ui.plainTextEdit.appendPlainText(
                    "Correct usage: grep [filename] [text_to_find]"
                )
            else:
                file_name = command[1]
                search_text = " ".join(command[2:])
                COMMANDS[cmd](file_name, search_text, self.ui)
        elif cmd == "rename":
            file_name: str = " ".join(command[1:])
            if not file_name:
                self.ui.plainTextEdit.appendPlainText("Invalid file name.")
            else:
                new_name, ok = QInputDialog.getText(
                    self, "Rename File", "Enter new name:"
                )
                COMMANDS[cmd](file_name, new_name, ok, self.ui)
        elif cmd == "renamedir":
            dir_name: str = " ".join(command[1:])
            if not dir_name:
                self.ui.plainTextEdit.appendPlainText("Invalid directory name.")
            else:
                new_name, ok = QInputDialog.getText(
                    self, "Rename Directory", "Enter new name:"
                )
                COMMANDS[cmd](dir_name, new_name, ok, self.ui)
        elif cmd in ("write", "rewrite"):
            file_name: str = " ".join(command[1:])
            if not file_name:
                self.ui.plainTextEdit.appendPlainText("Invalid file name.")
            else:
                dialog_title = "Append Text" if cmd == "write" else "Overwrite File"
                text, ok = QInputDialog.getText(self, dialog_title, "Enter text:")
                COMMANDS[cmd](file_name, text, ok, self.ui)
        elif cmd == "set":
            if num_args < 3:
                self.ui.plainTextEdit.appendPlainText(
                    "Wrong usage. Use: set color [#HEX] or set font [size]"
                )
            else:
                sub_cmd = command[1].lower()

                if sub_cmd == "color":
                    hex_color = command[2]
                    if hex_color.startswith("#") and len(hex_color) in (4, 7):
                        self._terminal_foreground = hex_color
                        self._apply_dynamic_style()
                        self.ui.plainTextEdit.appendPlainText(
                            f"Terminal text color changed to {hex_color}."
                        )
                    else:
                        self.ui.plainTextEdit.appendPlainText(
                            "Invalid HEX color. Example: set color #00ffcc"
                        )

                elif sub_cmd == "font":
                    try:
                        size = int(command[2])
                        if 9 <= size <= 24:
                            self._terminal_font_size = size
                            self._apply_dynamic_style()
                            self.ui.plainTextEdit.appendPlainText(
                                f"Terminal font size changed to {size}px."
                            )
                        else:
                            self.ui.plainTextEdit.appendPlainText(
                                "Font size must be between 9 and 24."
                            )
                    except ValueError:
                        self.ui.plainTextEdit.appendPlainText(
                            "Invalid size. Please enter a number. Example: set font 14"
                        )
                else:
                    self.ui.plainTextEdit.appendPlainText(
                        f"Unknown set option: '{sub_cmd}'. Use 'color' or 'font'."
                    )
        else:
            # Commands registered in COMMANDS but with an unexpected argument
            # count (e.g. `list foo`) end up here instead of silently misfiring.
            self.ui.plainTextEdit.appendPlainText(
                f"Wrong usage of '{cmd}'. Type 'help' for the correct syntax."
            )

        Util.current_dir(self.ui)  # refresh current dir display after any command
        return 0
