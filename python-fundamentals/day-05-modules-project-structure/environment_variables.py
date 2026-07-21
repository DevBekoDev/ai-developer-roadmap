import os


username = os.environ.get(
    "APP_USERNAME",
    "Guest",
)

print(f"Username: {username}")