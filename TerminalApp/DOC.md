# File and Directory Management Program

## Overview

This program provides a command-line interface for managing files and directories.
It allows users to create, read, write, rename, delete files and directories, change directories,
list files, and display help information.

## Commands

### The program supports the following commands:

-   mk: Create a new file -> Ex: mk file.py
-   read: Read the contents of a file -> Ex: read filename
-   write: Write to a file -> Ex: write filename, then a box will appear to insert the text
-   rewrite: Rewrite the contents of a file -> Ex: rewrite filename, then a box will appear to insert the text
-   delete: Delete a file -> Ex: delete filename
-   rename: Rename a file -> Ex: rename filename, then a box will appear to insert the new name
-   size: Display the size of a file -> Ex: size filename
-   mkdir: Create a new directory -> Ex: mkdir dirname
-   deletedir: Delete a directory -> Ex: deletedir dirname
-   renamedir: Rename a directory -> Ex: renamedir dirname, then a box will appear to insert the new name
-   dirsize: Display the size of a directory -> Ex: dirsize dirname
-   change: Change the current directory -> Ex: change dirname
-   list: List the files in the current directory -> Ex: list
-   help: Display help information -> Ex: help
-   about: Display information about the program -> Ex: about
-   clear: clear command-line interface -> Ex: clear

### Usage

To use the program, simply type a command followed by any required arguments.
For example, to create a new file called "example.txt", you would type mk example.txt.

## Functions

### The program uses the following functions to perform the various commands:

-   file.create(name): Create a new file with the given name
-   file.read(name): Read the contents of the file with the given name
-   file.write(name, contents): Write the given contents to the file with the given name
-   file.rewrite(name, contents): Rewrite the contents of the file with the given name
-   file.type(name): Display the type of the file with the given name
-   file.delete(name): Delete the file with the given name
-   file.rename(name, new_name): Rename the file with the given name to the given new name
-   file.size(name): Display the size of the file with the given name
-   folder.create(name): Create a new directory with the given name
-   folder.delete(name): Delete the directory with the given name
-   folder.rename(name, new_name): Rename the directory with the given name to the given new name
-   folder.size(name): Display the size of the directory with the given name
-   folder.change(name): Change the current directory to the given name
-   util.list_files(): List the files in the current directory
-   util.helper(): Display help information
-   util.about(): Display information about the program

## Requirements

-   Python 3.x
-   os module
-   utilities module (included in the project)
-   FileMethods module (included in the project)
-   FolderMethods module (included in the project)

## Installation

To install the program, simply copy the main.py file and the utilities, FileMethods, and FolderMethods
modules to a directory on your system. You can then run the program by executing the main.py file.

## License

This program is released under the MIT License. See the LICENSE file for details.
