HTTP_METHODS = {
    "GET": {
        "purpose": "Retrieve existing data",
        "example": "Get a list of AI models",
    },
    "POST": {
        "purpose": "Create new data",
        "example": "Create a new user account",
    },
    "PUT": {
        "purpose": "Replace an existing resource completely",
        "example": "Replace all information about a user",
    },
    "PATCH": {
        "purpose": "Update part of an existing resource",
        "example": "Change only a user's email address",
    },
    "DELETE": {
        "purpose": "Remove existing data",
        "example": "Delete a user account",
    },
}


for method, information in HTTP_METHODS.items():
    print(f"Method: {method}")
    print(f"Purpose: {information['purpose']}")
    print(f"Example: {information['example']}")
    print("-" * 40)