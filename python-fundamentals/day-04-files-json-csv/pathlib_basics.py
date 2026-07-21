from pathlib import Path


current_folder = Path.cwd()

print(f"Current folder: {current_folder}")


data_folder = current_folder / "data"

print(f"Data folder path: {data_folder}")


data_folder.mkdir(exist_ok=True)


notes_file = data_folder / "notes.txt"

print(f"Notes file path: {notes_file}")


print(f"Data folder exists: {data_folder.exists()}")
print(f"Notes file exists: {notes_file.exists()}")
print(f"Is data_folder a directory: {data_folder.is_dir()}")
print(f"Is notes_file a file: {notes_file.is_file()}")