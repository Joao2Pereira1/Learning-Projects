from os import getcwd  # only using one method no need to import the everything
from typing import List

from PyQt5.QtWidgets import *
from ui.my_gui import Ui_MainWindow  # UI design for the application
from utils.commands import COMMANDS
from utils.utilities import Util  # Extra methods ex: about, help, list
from utils.valid_args import valid_num_args


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

        # * Event handlers

        # display
        Util.current_dir(self, self.ui)  # display current dir
        
        # buttons
        self.ui.pushButton.clicked.connect(self.handle_input)  # clicking button
        self.ui.lineEdit.returnPressed.connect(self.handle_input)  #  Enter key

    def handle_input(self) -> int:
        """ Handles the user input and executes the corresponding command."""

        Util.current_dir(self, self.ui)  # display current dir

        command: List[str] = self.ui.lineEdit.text().split()  # get arguments
        num_args: int = len(command)
        for i in range(num_args):
            command[i] = command[i].lower()

        self.ui.lineEdit.setText("")  # clear text

        if valid_num_args(num_args, self.ui):
            pass
        else:
            return 0

        cmd: str = command[0]

        if cmd in COMMANDS:
            if num_args == 1 and cmd in ["list","help","clear","about"]:
                COMMANDS[cmd](self, self.ui)
            elif cmd in [
                "mk",
                "read",
                "delete",
                "size",
            ]:  # file commands

                file_name: str = " ".join(command[1:])  # file/dir name
                if file_name:
                    COMMANDS[cmd](self, file_name, self.ui)
                else:
                    self.ui.plainTextEdit.setPlainText("Invalid file name.")
            elif cmd in [
                "change",
                "mkdir",
                "deletedir",
                "dirsize",
            ]:  # directory commands

                dir_name: str = " ".join(command[1:])  #  dir_name
                if dir_name:
                    COMMANDS[cmd](self, dir_name, self.ui)
                else:
                    self.ui.plainTextEdit.setPlainText("Invalid directory name.")
            elif cmd == "renamedir":
                name: str = " ".join(command[1:])  #  file/dir name
                new_name, ok = QInputDialog.getText(
                    self, "Rename Directory", "Enter name:"
                )  # Ask for new name using QInputDialog
                COMMANDS[cmd](self, name, new_name, ok, self.ui)
            # remaining commands: write and rewrite
            else:
                name = " ".join(command[1:])  #  file/dir name
                text, ok = QInputDialog.getText(
                    self, "Add text to file", "Enter text:"
                )  # Ask for text using QInputDialog
                COMMANDS[cmd](self, name, text, ok, self.ui)
        else:
            self.ui.plainTextEdit.setPlainText("Invalid command. Please try again.")

        return 0
