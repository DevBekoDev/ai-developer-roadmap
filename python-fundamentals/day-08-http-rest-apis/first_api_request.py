import requests


API_URL = "https://jsonplaceholder.typicode.com/posts/1"


try:
    response = requests.get(API_URL, timeout=10)

    print(f"Status code: {response.status_code}")

    response.raise_for_status()

    post = response.json()

    print("\nPost received successfully:")
    print(f"Post ID: {post['id']}")
    print(f"User ID: {post['userId']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")

except requests.exceptions.Timeout:
    print("The request took too long and timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API. Check your internet connection.")

except requests.exceptions.RequestException as error:
    print(f"API request failed: {error}")