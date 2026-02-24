# 🧰 Python Utilities

This repository contains a small collection of utility functions written in Python, along with comprehensive tests using `pytest`. These utilities cover everyday tasks such as parsing dynamic routes, extracting data from query strings, and converting Brazilian postal codes (CEP) to city and state using the ViaCEP API.

---

## 📦 Features

- 🔢 **Dynamic Route Parser** – Convert route patterns like `/user/:id` into regex with named groups.
- 🏙️ **CEP to City/State Lookup** – Fetch city and state information from a Brazilian postal code.
- 🔍 **Query Parameter Extraction** – (More in progress: e.g., `extract_query_params.py`)
- 🎯 All functions are unit tested with `pytest`.
- 🧪 Type-safe with `mypy`.

---

## Geting Started

- After clonning the repo you must create a virtual environment
```bash
python3 -m venv .venv
```

- Then activate it:
```bash
source .venv/bin/activate
```

- now you can install the requirements:
```bash
pip install -r requirements.txt
```

- and run the tests to certificate everything is in order
```bash
pytest -q
```