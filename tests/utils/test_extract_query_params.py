import pytest
from src.utils.extract_query_params import extract_query_params


def test_if_can_extract_query_params():
    query = "?name=john&age=30"
    expected_result = {"name": "john", "age": "30"}

    result = extract_query_params(query)

    assert "name" in result and "age" in result
    assert result["name"] == expected_result["name"]
    assert result["age"] == expected_result["age"]


def test_if_query_without_questionmark_returns_error():
    query = "name=john"

    with pytest.raises(ValueError) as excinfo:
        extract_query_params(query)
    assert str(excinfo.value) == "Invalid query string"


def test_query_with_missing_equal_sign():
    query = "?name&john"

    with pytest.raises(ValueError) as excinfo:
        extract_query_params(query)
    assert str(excinfo.value) == "Invalid query parameter: missing '=' or value"


def test_query_with_key_but_no_value():
    query = "?name="

    with pytest.raises(ValueError) as excinfo:
        extract_query_params(query)
    assert str(excinfo.value) == "Invalid query parameter: missing '=' or value"
