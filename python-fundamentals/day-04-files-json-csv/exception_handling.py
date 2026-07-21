from pathlib import Path
import json


data_folder = Path.cwd() / "data"


# --------------------------------------------------
# EXAMPLE 1: FILE NOT FOUND
# --------------------------------------------------

missing_file = data_folder / "missing_file.txt"

try:
    content = missing_file.read_text(encoding="utf-8")
    print(content)

except FileNotFoundError:
    print("Error: The requested file does not exist.")


print()


# --------------------------------------------------
# EXAMPLE 2: INVALID NUMBER CONVERSION
# --------------------------------------------------

user_input = "25"

try:
    age = int(user_input)
    print(f"Age: {age}")

except ValueError:
    print("Error: Age must be a valid number.")


print()


# --------------------------------------------------
# EXAMPLE 3: INVALID JSON
# --------------------------------------------------

json_file = data_folder / "broken_data.json"

json_file.write_text(
    '{"username": "abubakr", "active": true',
    encoding="utf-8"
)

try:
    with json_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print(data)

except json.JSONDecodeError:
    print("Error: The JSON file contains invalid JSON.")


print()


# --------------------------------------------------
# EXAMPLE 4: ELSE AND FINALLY
# --------------------------------------------------

valid_file = data_folder / "ai_notes.txt"

try:
    content = valid_file.read_text(encoding="utf-8")

except FileNotFoundError:
    print("Error: ai_notes.txt was not found.")

else:
    print("File loaded successfully.")
    print(f"Characters in file: {len(content)}")

finally:
    print("File operation finished.")