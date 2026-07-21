from pathlib import Path


data_folder = Path.cwd() / "data"
data_folder.mkdir(exist_ok=True)

notes_file = data_folder / "ai_notes.txt"


# Write text to the file
notes_file.write_text(
    "AI engineering combines software engineering and artificial intelligence.\n"
    "Python is commonly used for AI development.\n"
    "Clean code makes AI systems easier to maintain.",
    encoding="utf-8"
)


# Read all text from the file
content = notes_file.read_text(encoding="utf-8")

print("Full file content:")
print(content)


# Add more text without deleting the existing content
with notes_file.open("a", encoding="utf-8") as file:
    file.write("\nObject-oriented programming helps organize larger applications.")


print()
print("Updated file content:")

updated_content = notes_file.read_text(encoding="utf-8")

print(updated_content)