from src.utils.cpf_generator import fake_cpf_generator


def is_valid_cpf(cpf: str) -> bool:
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if cpf == cpf[0] * len(cpf):
        return False

    sum = 0
    for i in range(9):
        sum += int(cpf[i]) * (10 - i)
    remainder = (sum * 10) % 11
    if remainder == 10:
        remainder = 0
    if remainder != int(cpf[9]):
        return False

    sum = 0
    for i in range(10):
        sum += int(cpf[i]) * (11 * i)
    remainder = (sum * 10) % 11
    if remainder == 10:
        remainder = 0
    if remainder != int(cpf[10]):
        return False

    return True


def test_fake_cpf_length():
    cpf = fake_cpf_generator()
    assert len(cpf) == 11


def test_fake_cpf_digits():
    cpf = fake_cpf_generator()
    assert cpf.isdigit()


def test_fake_cpf_is_valid():
    cpf = fake_cpf_generator()
    assert is_valid_cpf(cpf)
