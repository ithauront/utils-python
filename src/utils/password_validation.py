import re


def validate_password(password: str) -> None:
    if not password:
        raise ValueError("password_required")
    if " " in password:
        raise ValueError("password_cannot_contain_spaces")
    if len(password) < 8:
        raise ValueError("password_too_short")
    if not re.search(r"[A-Z]", password):
        raise ValueError("password_needs_uppercase")
    if not re.search(r"[a-z]", password):
        raise ValueError("password_needs_lowercase")
    if not re.search(r"[0-9]", password):
        raise ValueError("password_needs_number")
