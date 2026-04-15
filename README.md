# 🧰 Python Utilities

This repository contains a small collection of utility functions written in Python, along with comprehensive tests using `pytest`. These utilities cover everyday tasks such as parsing dynamic routes, extracting data from query strings, and converting Brazilian postal codes (CEP) to city and state using the ViaCEP API.

---

## 📦 Features

This repository includes utilities for:

### 🔢 Data validation & generation
- Brazilian CPF generator (`cpf_generator.py`)
- Brazilian phone number validation (`brazilian_phone_number_validation.py`)
- Username validation (`username_validation.py`)
- Password validation (`password_validation.py`)

### 🏙️ Location & Brazilian data
- CEP (postal code) to city/state lookup using ViaCEP (`cep_to_city_and_state.py`)

### 🔍 Data parsing & extraction
- Query parameter extraction (`extract_query_params.py`)
- Regex-based utilities (`regex/` module)

### ✂️ Text processing
- Split text into chunks without breaking words (`split_text_into_chunks.py`)
- Trim text to last complete word (`trim_to_last_word.py`)

---

## 🧪 Testing

All utilities are fully tested using `pytest`.

Run tests with:
```bash
pytest -q
```

🧪 Type Checking

This project uses mypy for static type checking:
```bash
mypy .
```

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