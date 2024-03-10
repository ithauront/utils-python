import pytest
from src.utils.cep_to_city_and_state import cep_to_city_and_state, InvalidCepError


def test_if_transform_cep_to_city_and_state():
    cep = "01001-000"
    expected_result = {"city": "São Paulo", "state": "SP"}

    result = cep_to_city_and_state(cep)

    assert "city" in result and "state" in result
    assert result["city"] == expected_result["city"]
    assert result["state"] == expected_result["state"]


def test_if_invalid_cep_returns_error():
    cep = "invalid cep"

    with pytest.raises(InvalidCepError):
        cep_to_city_and_state(cep)
