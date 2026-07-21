import json
from pathlib import Path


data_folder = Path.cwd() / "data"
data_folder.mkdir(exist_ok=True)

json_file = data_folder / "users.json"


users = [
    {
        "username": "abubakr",
        "email": "abubakr@example.com",
        "active": True
    },
    {
        "username": "sara",
        "email": "sara@example.com",
        "active": False
    }
]


# Write Python data to a JSON file
with json_file.open("w", encoding="utf-8") as file:
    json.dump(
        users,
        file,
        indent=4
    )


# Read JSON data back into Python
with json_file.open("r", encoding="utf-8") as file:
    loaded_users = json.load(file)


print("Loaded users:")

for user in loaded_users:
    print(
        f"{user['username']} - "
        f"{user['email']} - "
        f"Active: {user['active']}"
    )


print()

# Add another user
new_user = {
    "username": "ahmed",
    "email": "ahmed@example.com",
    "active": True
}

loaded_users.append(new_user)


# Save the updated list
with json_file.open("w", encoding="utf-8") as file:
    json.dump(
        loaded_users,
        file,
        indent=4
    )


print("Updated users:")

for user in loaded_users:
    print(user)