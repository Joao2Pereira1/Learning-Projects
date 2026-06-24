""" Module for displaying to do list text """

from PyQt5.QtWidgets import QWidget


class ToDoListView:
    """Class for displaying to do list text"""

    def __init__(self, window: QWidget) -> None:
        self.window = window

    def clear_tasks(self) -> None:
        """Clears the to do list text in the given window"""

        self.window.TextBox.setPlainText("")

    def display_last_tasks(self, history: str) -> None:
        """Displays the last tasks in the given window"""

        self.window.TextBox.setPlainText(history.replace(", ", "\n"))

    def clear_text_box(self) -> None:
        """Clears the text box in the given window"""

        self.window.Text.setText("")
