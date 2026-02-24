import pytest

from src.utils.password_validation import validate_password


def test_password_validaton_success():
    password = "Jhon_doe-1."
    validate = validate_password(password)

    assert validate is None


def test_password_not_sent():
    password = ""
    with pytest.raises(ValueError, match="password_required"):
        validate_password(password)


def test_password_with_spaces():
    password = "Jhon doe 1."
    with pytest.raises(ValueError, match="password_cannot_contain_spaces"):
        validate_password(password)


def test_password_too_short():
    password = "JhonDoe"
    with pytest.raises(ValueError, match="password_too_short"):
        validate_password(password)


def test_password_without_uppercase():
    password = "jhondoe1"
    with pytest.raises(ValueError, match="password_needs_uppercase"):
        validate_password(password)


def test_password_without_letters():
    password = "123456789"
    # The first verification for letter is the need of uppercase
    with pytest.raises(ValueError, match="password_needs_uppercase"):
        validate_password(password)


def test_password_without_lowercase():
    password = "JHONDOE1"
    with pytest.raises(ValueError, match="password_needs_lowercase"):
        validate_password(password)


def test_password_without_number():
    password = "Jhon_doe-!"
    with pytest.raises(ValueError, match="password_needs_number"):
        validate_password(password)
