# To-Do App Project Documentation

## Overview

The To-Do App is a task management system designed to help users organize and prioritize their daily tasks. The app allows users to create, edit, and delete tasks, as well as mark them as completed.

## Features

-   Task Creation: Users can create new tasks with a title.
-   Task Management: Users can view and edit their tasks.
-   Task Storage: Tasks are stored in a file for persistence.
-   User Interface: The app has a user-friendly interface built with PyQt5.
-   Shortcuts: The app provides shortcuts for saving, clearing, and exiting the application.
-   Welcome Dialog: The app displays a welcome dialog box asking the user to enter their name.
-   Technical Requirements
-   Frontend: The app is built using PyQt5 for the user interface.
-   Backend: The app uses Python for the logic and file storage.
-   Storage: Tasks are stored in a file named data.txt in the models directory.

## User Stories

-   As a user, I want to be able to create a new task so that I can keep track of my to-do list.
-   As a user, I want to be able to view my tasks so that I can stay organized.
-   As a user, I want to be able to edit my tasks so that I can update their details.
-   As a user, I want to be able to delete my tasks so that I can remove unnecessary tasks from my list.
-   As a user, I want to be able to save my tasks so that I can retrieve them later.
-   As a user, I want to be able to clear my task list so that I can start fresh.

## Classes and Methods

### MainWindowController Class

-   **init**: Initializes the class instance with a user interface, sets up event handlers, and connects button and text input signals to specific functions.
-   on_button_clicked: Captures user input, adds it to a todo list, updates the UI, stores the todo list in a file, and handles potential IO errors.
-   last_session: Gets the todo list from the last session and stores it in a file.
-   display_last_session: Loads the todo list from the file and displays it in the UI.
-   clear_session: Clears the todo list and history file.
-   dialog: Displays an input dialog box asking the user to enter their name, and if the cancel button is pressed, it exits the application.

### TodoList Class (Data Management)

-   add_todo: Adds a new task to the todo list.
-   get_todo_items: Returns the todo list as a string.
-   storing_todos: Stores the todo list to a file.

### Shortcuts Class

-   save: Saves the todo list to a file.
-   clear: Clears the todo list and history file.
-   exit: Exits the application.

## Wireframes

[Insert wireframes of the app's UI, including the task list, task creation form, and task details page]

## Database Schema

[Insert database schema, including the tasks collection and its fields]

## API Endpoints

[Insert API endpoints, including the create task, read task, update task, and delete task endpoints]

This documentation provides an overview of the To-Do App project, its features, technical requirements, user stories, classes, and methods. It also includes sections for wireframes, database schema, and API endpoints, which can be added or removed as needed.
