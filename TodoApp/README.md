# ✅ To-Do App

## Overview

The **To-Do App** is a desktop task management application developed in **Python** using **PyQt5**. It allows users to create and manage a personal to-do list through a graphical interface while automatically saving tasks between sessions.

The application focuses on simplicity and usability, providing an intuitive interface with keyboard shortcuts and persistent local storage.

---

# Features

- Create new tasks
- Display all saved tasks
- Automatically save tasks locally
- Restore tasks from the previous session
- Clear the entire task list
- Keyboard shortcuts for common actions
- Simple and responsive PyQt5 graphical interface

---

# How It Works

1. The application starts by displaying a welcome dialog asking for the user's name.
2. Existing tasks are loaded from the previous session.
3. The user enters a new task and presses **Add**.
4. The task is immediately displayed in the interface.
5. Tasks can be saved at any time or automatically when required.
6. The task list can be cleared, removing both the interface contents and the saved history.

---

# Technologies Used

| Technology        | Purpose                               |
| ----------------- | ------------------------------------- |
| Python 3          | Application logic                     |
| PyQt5             | Graphical User Interface              |
| Text File Storage | Persistent task storage               |
| Qt Designer       | User interface design (if applicable) |

---

# Data Storage

The application stores all tasks inside:

```text
models/data.txt
```

Each task is written to the file so that it can be restored when the application is opened again.

---

# Shortcuts

Provides keyboard shortcuts for common operations.

| Shortcut                      | Action           |
| ----------------------------- | ---------------- |
| Ctrl + S                      | Save tasks       |
| Ctrl + L _(or your shortcut)_ | Clear task list  |
| Ctrl + Q                      | Exit application |

---

# Error Handling

The application handles common file input/output exceptions, including:

- Missing storage file
- File read errors
- File write errors

This prevents unexpected crashes during normal operation.

---

# Requirements

- Python 3.10+
- PyQt5

Install dependencies:

```bash
pip install PyQt5
```

---

# Running the Application

```bash
python main.py
```
---

# License

This project is distributed under the MIT License.

---

# License

This project is available under the MIT License.
