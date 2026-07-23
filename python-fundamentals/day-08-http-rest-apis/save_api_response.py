import json
from pathlib import Path

import requests


API_URL = "https://jsonplaceholder.typicode.com/posts/1"
OUTPUT_FILE = Path(__file__).parent / "data" / "post_1.json"


try:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    post = response.json()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(post, file, indent=4, ensure_ascii=False)

    print("API response saved successfully.")
    print(f"File location: {OUTPUT_FILE}")

except requests.exceptions.Timeout:
    print("The request took too long and timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API. Check your internet connection.")

except requests.exceptions.RequestException as error:
    print(f"API request failed: {error}")

except OSError as error:
    print(f"Could not save the JSON file: {error}")