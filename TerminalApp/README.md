# 📂 File and Directory Management Program

## Overview

This program provides an interactive command-line interface (CLI) for managing files and directories on your system. It simplifies common file system tasks by allowing users to create, read, write, rename, and delete both files and directories, track sizes, change working directories, and inspect contents.

---

## Commands

To use the program, type the command followed by any required arguments.

### Usage Example

To create a new text file:

```bash
mk example.txt
```

### Supported CLI Commands

| Command | Action | Example Syntax |
|---------|--------|----------------|
| `mk` | Create a new file | `mk file.py` |
| `read` | Read the contents of a file | `read filename` |
| `write` | Append text to a file (opens a text input box) | `write filename` |
| `rewrite` | Overwrite the contents of a file (opens a text input box) | `rewrite filename` |
| `delete` | Delete a file | `delete filename` |
| `rename` | Rename a file (opens a text input box for the new name) | `rename filename` |
| `size` | Display the size of a file | `size filename` |
| `mkdir` | Create a new directory | `mkdir dirname` |
| `deletedir` | Delete a directory | `deletedir dirname` |
| `renamedir` | Rename a directory (opens a text input box for the new name) | `renamedir dirname` |
| `dirsize` | Display the total size of a directory | `dirsize dirname` |
| `change` | Change the current working directory | `change dirname` |
| `list` | List all files in the current directory | `list` |
| `help` | Display manual and help information | `help` |
| `about` | Display metadata and information about the program | `about` |
| `clear` | Clear the command-line interface screen | `clear` |

---

## Technical Functions

The CLI translates user inputs directly into the following backend functions.

### File Management (`FileMethods` Module)

| Function | Description |
|----------|-------------|
| `file.create(name)` | Creates a new file with the given name. |
| `file.read(name)` | Reads and outputs the text contents of the specified file. |
| `file.write(name, contents)` | Appends the provided content to the specified file. |
| `file.rewrite(name, contents)` | Replaces the existing file content with the new text. |
| `file.type(name)` | Analyzes and displays the file extension/type. |
| `file.delete(name)` | Permanently removes the specified file. |
| `file.rename(name, new_name)` | Renames the specified file. |
| `file.size(name)` | Calculates and displays the file size. |

### Folder Management (`FolderMethods` Module)

| Function | Description |
|----------|-------------|
| `folder.create(name)` | Creates a new directory. |
| `folder.delete(name)` | Deletes the specified directory. |
| `folder.rename(name, new_name)` | Renames the specified directory. |
| `folder.size(name)` | Calculates the total size of the directory. |
| `folder.change(name)` | Changes the current working directory. |

### Core Utilities (`utilities` Module)

| Function | Description |
|----------|-------------|
| `util.list_files()` | Lists the contents of the current directory. |
| `util.helper()` | Displays the help menu. |
| `util.about()` | Displays application metadata and build information. |

---

## System Requirements

Ensure your environment includes:

- Python 3.x
- `os` module (Python standard library)
- `utilities` module (included in the project)
- `FileMethods` module (included in the project)
- `FolderMethods` module (included in the project)

---

## Installation & Execution

1. Copy the following files into the same directory:
   - `main.py`
   - `utilities.py`
   - `FileMethods.py`
   - `FolderMethods.py`

2. Run the application:

```bash
python main.py
```

---

## License

This project is open-source and distributed under the **MIT License**. See the `LICENSE` file for complete licensing information.
