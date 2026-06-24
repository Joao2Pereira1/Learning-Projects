from PyQt5.QtWidgets import QAction


class Shortcuts:
    """The class 'Shortcuts' provide shortcuts and buttons to save session,
    clear session, and exit program"""

    def __init__(self, window) -> None:
        self.window = window

    def save(self) -> None:
        """
        Creates a menu item and shortcut for saving the to do list in a
        PyQt application.
        """

        self.window.saveAction = QAction("Save", None)
        self.window.saveAction.setShortcut("Ctrl+S")
        self.window.saveAction.triggered.connect(self.window.save_last_session)

        # Add the action to a menu
        menubar = self.window.menuBar()
        menubar.addAction(self.window.saveAction)

    def clear(self) -> None:
        """
        Creates a menu item and shortcut for clearing the to do list in a
        PyQt application.
        """

        self.window.clearAction = QAction("Clear", None)
        self.window.clearAction.setShortcut("Ctrl+D")
        self.window.clearAction.triggered.connect(self.window.clear_session)

        # Add the action to a menu
        menubar = self.window.menuBar()
        menubar.addAction(self.window.clearAction)

    def exit(self) -> None:
        """
        Creates a menu item and shortcut for exiting the application in a
        PyQt application.
        """

        self.window.exitAction = QAction("Exit", None)
        self.window.exitAction.setShortcut("Ctrl+Q")
        self.window.exitAction.triggered.connect(self.window.close)

        # Add the action to a menu
        menubar = self.window.menuBar()
        menubar.addAction(self.window.exitAction)
