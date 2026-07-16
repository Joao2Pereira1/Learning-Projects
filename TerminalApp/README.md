# ⚡ Flash Terminal

A desktop application built in **Python** with **PyQt5**, simulating an interactive terminal interface for safe and advanced local file system navigation. The project follows strict Model-View-Controller (MVC) architecture, implements a dynamic runtime style engine, features system command autocompletion, and serializes user session preferences via a persistent JSON file.

## Overview & Functionality

This application is a practical desktop system utility designed to test raw command-line text parsing, runtime stylesheet injection, interactive keyboard event monitoring, and dynamic persistent configurations in a graphical environment.

- **Core Feature:** The user inputs text expressions into a terminal line. Upon submission, the app parses the input to match backend actions, rendering the output in real time.

- **Persistent Sessions:** User preferences (background color, text hex codes, and font scaling parameters) are kept safe across application restarts along with a continuous keyboard command history buffer.

- **Parameter & Command Validation:** Instead of a generic input checker, each command is evaluated individually. The controller identifies the command, verifies the exact number of required arguments, and validates their format. This targeted validation prevents crashes and ensures complex, multi-word inputs are processed without being cut off.

## User Interface (Qt)

The graphical user interface was initially designed visually using **Qt Designer** and some details were changed through code.

### Interface Architecture (Main Window)

```
MainWindow
│
├── menubar (Top Menu)
│   ├── themeMenu (Themes)
│   │   ├── actionMatrixGreen
│   │   ├── actionClassicWhite
│   │   └── actionDraculaPurple
│   │
│   └── fontMenu (Font Size)
│       ├── actionFontSmall
│       ├── actionFontNormal
│       └── actionFontLarge
│
└── centralwidget
    └── mainLayout (Vertical Alignment)
         │
         ├── plainTextEdit (Terminal Output Display Box)
         │
         ├── inputLayout (Horizontal Line Alignment)
         │   ├── promptLabel (Displays ">")
         │   ├── lineEdit (Text Input Area)
         │   └── pushButton (Send/Execute Trigger)
         │
         └── currentDirLabel (Status Bar displaying: "Current directory: [PATH]")
```

### Key UI Workflows

- **Command Submission:** The user types an instruction into `lineEdit` and presses *Enter* or clicks `pushButton`. This clears the input area, records the sequence into the historical stack, and echoes the output to `plainTextEdit`.

- **Keyboard Event Filtering:** Intercepts native application window keypress events. Pushing **ArrowUp** or **ArrowDown** navigates backward and forward through previous command memories. Pushing **Tab** matches strings against known registers using a case-insensitive `QCompleter`.

- **Input Drafting Cache:** If the user drafts an incomplete text string and browses history using directional keys, the program buffers that uncommitted draft into a memory cache, restoring it safely if the user backtracks.

- **Dynamic QSS Overwrites:** Dynamic customization, by applying modified CSS strings containing user color choices, and performing hard refreshes to override active skins seamlessly.

## Project Structure

The folder and file organization follows the **MVC (Model-View-Controller)** pattern to decouple business logic, interface, and data-consuming services.

```
app/
│
├── controller/
│   └── main_window_controller.py   # Connects the UI to utilities, manages event loops, key filters, and style updates
│
├── styles/
│   └── styles.qss                  # Application baseline cascading stylesheet rules
│
├── ui/
│   ├── my_gui.py                   # Interface layout code compiled from Qt Designer (pyuic5)
│   └── my_gui.ui                   # Qt Designer visual workspace blueprint XML file
│
├── utils/
│   ├── commands.py                 # Mapping dictionary linking terminal token verbs to back-end execution scripts
│   ├── settings_handler.py         # Encapsulates file operations to save/load history arrays and theme details
│   └── utilities.py                # Functional core for core commands (list, about, clear, help)
│
├── data/                            # Folder reserved for system data storage and state outputs
│   ├── terminal_settings.json      # Serialized data configuration file for skin configurations and logs
│   └── task_list.txt               # Content files modified dynamically by system file routines
│
├── resources/
│   └── icons/
│       └── lighting.jpg            # Main operating system window application icon
│
├── docs/
│   ├── layout_qt.md                # Visual components structural alignment map
│   └── file_structure.md           # Complete overview of project file architecture and boundaries
│
├── main.py                         # Application entry point that handles boot paths and triggers the event loop
└── requirements.txt                # Project python dependencies index
```

### Available Commands

| **Command Trigger** | **Target Object** | **Action Performed**                                | **Example Syntax**     |
| ------------------- | ----------------- | --------------------------------------------------- | ---------------------- |
| `mk`                | File              | Creates a brand new file                            | `mk script.py`         |
| `read`              | File              | Outputs text lines from a target file               | `read index.html`      |
| `write`             | File              | Appends message text to a file via popup box        | `write logs.txt`       |
| `rewrite`           | File              | Destroys file text and writes new input via popup   | `rewrite logs.txt`     |
| `delete`            | File              | Erases a file target permanently from path          | `delete temp.csv`      |
| `rename`            | File              | Changes target filename via input popup dialog      | `rename main.py`       |
| `size`              | File              | Displays total storage block weight in bytes        | `size asset.png`       |
| `mkdir`             | Directory         | Spins up a new directory structure                  | `mkdir assets`         |
| `deletedir`         | Directory         | Erases a folder node from the system path           | `deletedir old_build`  |
| `renamedir`         | Directory         | Alters a directory label via input popup dialog     | `renamedir old_assets` |
| `dirsize`           | Directory         | Computes combined weight of all internal files      | `dirsize media`        |
| `change`            | Directory         | Pivots operational working workspace paths          | `change templates`     |
| `find`              | Search            | Crawls the path trees looking for string matches    | `find .qss`            |
| `grep`              | Search            | Parses internal lines looking for character matches | `grep app.log "Error"` |
| `set color`         | Interface         | Injects runtime Hex values onto typography layers   | `set color #00ffcc`    |
| `set font`          | Interface         | Updates pixel dimensions on the terminal font face  | `set font 14`          |

#### Configuration Management (JSON Store Cache)

To guarantee that cosmetic setups and shell operations stay active between separate software launches, the system includes an absolute storage handler (`settings_handler`).

- **The Problem:** Relocating deep path structures using the `change` command causes file write actions using path symbols like `./` to drop files into the newly focused directory, leading to data loss and multiple duplicate configuration sheets.

- **The Solution (`settings_handler`):**
  
  1. Resolves coordinates down to the root script file location using `os.path.abspath(__file__)`.
  
  2. Anchors tracking definitions down to a permanent space under `app/data/`.
  
  3. **Read Cycle:** At launch, it reads `terminal_settings.json` to configure variables before components are painted onto the monitor layout.
  
  4. **Write Cycle:** Captures text modifications from inputs or click events from top menu bars, writing arrays back to the central secure file coordinates instantly.

## Requirements & Setup

### System Requirements

- **Python:** >= 3.8 (Utilizes absolute path resolution wrappers and native typing features.)

### Installing Dependencies

Project dependencies are declared in `requirements.txt`:

Plaintext

```
PyQt5
```

Install all required application dependencies with:

Bash

```
pip install -r requirements.txt
```

## How to Run the Project

1. **Verify Asset Directories:** Ensure the required structure is intact, noting that data stores like `app/data/` will automatically instantiate upon running the entry file if missing.

2. **Launch the Core Shell Loop:** Execute the absolute application entry point from your terminal interface:
   
   Bash
   
   ```
   python app/main.py
   ```

---

# License

This project is distributed under the MIT License.
