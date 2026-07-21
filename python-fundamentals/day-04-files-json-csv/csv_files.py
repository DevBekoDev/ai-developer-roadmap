import csv
from pathlib import Path


data_folder = Path.cwd() / "data"
data_folder.mkdir(exist_ok=True)

csv_file = data_folder / "users.csv"


users = [
    {
        "username": "abubakr",
        "email": "abubakr@example.com",
        "age": 23
    },
    {
        "username": "sara",
        "email": "sara@example.com",
        "age": 25
    },
    {
        "username": "ahmed",
        "email": "ahmed@example.com",
        "age": 28
    }
]


# Write data to CSV
with csv_file.open("w", newline="", encoding="utf-8") as file:
    fieldnames = ["username", "email", "age"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(users)


# Read data from CSV
with csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    loaded_users = list(reader)


print("Loaded users:")

for user in loaded_users:
    print(
        f"{user['username']} - "
        f"{user['email']} - "
        f"Age: {user['age']}"
    )


print()

# Add another row
new_user = {
    "username": "mona",
    "email": "mona@example.com",
    "age": 30
}

with csv_file.open("a", newline="", encoding="utf-8") as file:
    fieldnames = ["username", "email", "age"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writerow(new_user)


# Read the updated file
with csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    updated_users = list(reader)


print("Updated users:")

for user in updated_users:
    print(user)