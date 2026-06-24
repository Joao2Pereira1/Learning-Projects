import os

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASSWORD")

API_GPT = os.environ.get("API_KEY_GPT")

if __name__ == "__main__":
    print("You are on the main file")
