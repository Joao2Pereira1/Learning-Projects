"""
Summary:
    The `settings_handler` module manages the persistence of terminal settings
    and command history by saving and loading data from a JSON file located
    in the application's data directory.
"""

import json
import os

# Navigate up to the 'app' directory, then into the 'data' directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
SETTINGS_FILE = os.path.join(DATA_DIR, "terminal_settings.json")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)


def load_settings() -> dict:
    """
    Summary:
        Loads the configuration and history from the JSON file in the data folder.
    Returns:
        dict: default settings if the file does not exist or is corrupted.
    """
    default_settings = {
        "background": "#121214",
        "foreground": "#cbd5e1",
        "font_size": 16,
        "history": [],
    }

    if not os.path.exists(SETTINGS_FILE):
        return default_settings

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            for key, value in default_settings.items():
                if key not in data:
                    data[key] = value
            return data
    except Exception:
        return default_settings


def save_settings(bg: str, fg: str, font_size: int, history: list) -> None:
    """
    Summary:
        Saves the current terminal appearance and history into the JSON file in the data folder.
    """
    data = {
        "background": bg,
        "foreground": fg,
        "font_size": font_size,
        "history": history,
    }
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving settings: {e}")
