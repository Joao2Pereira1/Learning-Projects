from ui.my_gui import Ui_MainWindow


def valid_num_args(num_args: int, window: Ui_MainWindow) -> bool:
    """
    Checks if the number of arguments entered by the user is valid.

    Args:
        num_args (int): The number of arguments entered by the user.
        window (QWidget): The GUI window.

    Returns:
        bool: True if the number of arguments is valid (between 1 and 3), False otherwise.
    """

    if num_args > 3:
        window.plainTextEdit.setPlainText("Too many arguments")
        return False
    elif num_args == 0:
        window.plainTextEdit.setPlainText("No arguments")
        return False
    else:
        return True