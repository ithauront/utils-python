import requests


class InvalidCepError(Exception):
    """Exeption of Invalid CEP"""

    pass


def cep_to_city_and_state(cep: str) -> dict:
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        response.raise_for_status()

        data = response.json()
        if "erro" in data:
            raise InvalidCepError

        return {"city": data["localidade"], "state": data["uf"]}

    except requests.RequestException:
        raise InvalidCepError from None
    except Exception as error:
        print(error)
        raise Exception("Error acessing CEP service")
