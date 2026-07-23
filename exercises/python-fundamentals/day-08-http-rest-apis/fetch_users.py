import json
from pathlib import Path

import requests


API_URL = "https://jsonplaceholder.typicode.com/users"

OUTPUT_FILE = (
    Path(__file__).parent
    / "data"
    / "users.json"
)


def fetch_users() -> list[dict]:
    """Retrieve users from the API."""

    response = requests.get(
        API_URL,
        timeout=10,
    )

    response.raise_for_status()

    users = response.json()

    return users


def save_users(users: list[dict]) -> None:
    """Save the users to a JSON file."""

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            users,
            file,
            indent=4,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    try:
        users = fetch_users()

        save_users(users)

        print(
            f"{len(users)} users retrieved "
            "and saved successfully.\n"
        )

        for user in users:
            print(
                f"{user['name']} — "
                f"{user['email']}"
            )

    except requests.exceptions.Timeout:
        print(
            "The request took too long "
            "and timed out."
        )

    except requests.exceptions.ConnectionError:
        print(
            "Could not connect to the API. "
            "Check your internet connection."
        )

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")

    except OSError as error:
        print(f"Could not save the JSON file: {error}")