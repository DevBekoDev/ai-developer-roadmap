"""Utility functions for validating user input."""


def is_valid_email(email: str) -> bool:
    """Check whether an email address has a basic valid structure."""
    cleaned_email: str = email.strip()

    if cleaned_email.count("@") != 1:
        return False
    
    username, domain = cleaned_email.split("@")

    if not username or not domain:
        return False
    
    if "." not in domain:
        return False
    
    if domain.startswith(".") or domain.endswith("."):
        return False
    
    if username.startswith(".") or username.endswith("."):
        return False

    if ".." in username:
        return False

    return True

email_address: str = input("Enter an email address: ")

if is_valid_email(email=email_address):
    print("Valid email address.")
else:
    print("Invalid email address.")