HTTP_STATUS_CODES = {
    200: {
        "name": "OK",
        "meaning": "The request succeeded.",
    },
    201: {
        "name": "Created",
        "meaning": "A new resource was created successfully.",
    },
    204: {
        "name": "No Content",
        "meaning": "The request succeeded, but there is no response body.",
    },
    400: {
        "name": "Bad Request",
        "meaning": "The client sent invalid data.",
    },
    401: {
        "name": "Unauthorized",
        "meaning": "Authentication is required or incorrect.",
    },
    403: {
        "name": "Forbidden",
        "meaning": "The client is authenticated but does not have permission.",
    },
    404: {
        "name": "Not Found",
        "meaning": "The requested resource does not exist.",
    },
    429: {
        "name": "Too Many Requests",
        "meaning": "The client sent too many requests in a short time.",
    },
    500: {
        "name": "Internal Server Error",
        "meaning": "An unexpected error happened on the server.",
    },
    503: {
        "name": "Service Unavailable",
        "meaning": "The server is temporarily unavailable.",
    },
}


for code, information in HTTP_STATUS_CODES.items():
    print(f"Status code: {code}")
    print(f"Name: {information['name']}")
    print(f"Meaning: {information['meaning']}")
    print("-" * 50)