"""Modulo for controlling the app"""

from PyQt5.QtWidgets import QMainWindow

from app.model.todo_list import TodoList  # data list
from app.model.todo_list_file_handler import \
    TodoListFileHandler  # file operations
from app.ui.my_gui import Ui_MainWindow  # UI design for the application
from app.utils.shortcuts import Shortcuts  # app shortcuts
from app.view.todo_list_view import ToDoListView  # display tasks text

# < CONTROLLER


""" `MainWindowController` class in Python sets up a user interface for a
to do list application, handles user input, stores todo items in a file,
and provides functionality for viewing history and exiting the application. """


class MainWindowController(QMainWindow):

    def __init__(self):
        """
        self → the main window (QMainWindow) that will be displayed on the screen.

        Ui_MainWindow → the interface class created in Qt Designer.

        self.ui.setupUi(self) → method of the Ui_MainWindow class
        that takes a window (QMainWindow) as an argument and is responsible
        for adding the widgets created in Qt Designer
        into the main window (self).
        """

        super().__init__()  # herda QMainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # * Create classes instances

        self.todo_list = TodoList()
        self.view_list = ToDoListView(self.ui)
        self.shortcuts = Shortcuts(self)
        self.todo_file = TodoListFileHandler("./app/data/task_list.txt")

        # * Event handlers

        self.load_last_session()  # get the previous to do list
        self.handle_shortcuts()  # shortcuts

        # buttons
        self.ui.Button.clicked.connect(self.add_todo_item)
        self.ui.Text.returnPressed.connect(self.add_todo_item)

    # * shortcuts

    def handle_shortcuts(self):
        """Shortcut methods for the application."""

        self.shortcuts.save()  # save shortcut
        self.shortcuts.clear()  # clear shortcut
        self.shortcuts.exit()  # exit shortcut

    # *to do management

    def add_todo_item(self) -> None:
        """
        The function captures user input, adds it to a todo list, updates the UI,
        stores the todo list in a file, and handles potential IO errors.
        """

        #  Logic for button click
        new_todo_item = self.ui.Text.text()
        self.todo_list.add_todo(new_todo_item)  # adds todo to list
        self.ui.TextBox.setPlainText(self.todo_list.get_todo_items())  # update list

        self.view_list.clear_text_box()  # clear task inserted

        # * storing data into a file when button pressed
        self.todo_file.save_todo_list(self.todo_list.get_todo_items())

    def save_last_session(self) -> None:
        """Save todo from last session"""

        history = self.ui.TextBox.toPlainText()  # get to do list string
        self.todo_file.save_todo_list(history)  # save history to text file

    def load_last_session(self) -> None:
        """Load todos history from file when app starts"""

        history = self.todo_file.load_todo_list()
        self.view_list.display_last_tasks(history)  # load history from text file

    def clear_session(self) -> None:
        """Clear todo list and history file"""

        self.view_list.clear_tasks()  # clear tasks list

        self.todo_file.clear_todo_list_file()  # clear to do list text file
        self.todo_list.clear_list()  # clear to to list
