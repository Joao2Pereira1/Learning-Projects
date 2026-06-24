# #< DATA MANAGEMENT


class TodoList:
    """The `TodoList` class allows for adding, retrieving, and storing todo items in a list."""

    def __init__(self) -> None:
        """open file and get todos history"""

        history = ""
        try:
            with open("./app/data/task_list.txt", "r") as f:
                history = f.read()
        except IOError as e:
            print(f"Todo list couldn't access history file. {e}")
        finally:
            self.todos = [history]  # create a list for storing to dos

    def add_todo(self, todo: str) -> None:
        """Add a new todo item"""

        self.todos.append(todo)

    def get_todo_items(self) -> str:
        """return all todo items as a string"""

        return "\n".join(self.todos)

    def clear_list(self) -> list:
        """clear the list of todos"""

        self.todos = []
        return self.todos
