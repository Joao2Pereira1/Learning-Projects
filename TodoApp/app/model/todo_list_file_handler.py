# #< FILE HANDLING


class TodoListFileHandler:
    """The class 'TodoListFileHandler' is responsible for handling file operations
    like saving todo list to txt file, clearing text file, and others"""

    def __init__(self, file_path: str):
        """Initialize the file handler with a file path"""

        self.file_path = file_path

    def save_todo_list(self, todo_list: str) -> None:
        """Save the todo list to the file"""

        try:
            with open(self.file_path, "w") as f:
                f.write(todo_list)
        except IOError as e:
            print(f"Error saving todo list to file: {e}")

    def load_todo_list(self) -> str:
        """Load the todo list from the file"""

        try:
            with open(self.file_path, "r") as f:
                return f.read()
        except IOError as e:
            print(f"Error loading todo list from file: {e}")
            return ""

    def clear_todo_list_file(self) -> None:
        """Clear the todo list from the file"""

        try:
            with open(self.file_path, "w") as f:
                f.write("")
        except IOError as e:
            print(f"Error clearing todo list file: {e}")
