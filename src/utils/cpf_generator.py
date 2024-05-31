import random


def fake_cpf_generator():
    cpf = ''
    sum = 0

    for i in range(1, 10):
        digit = random.randint(0, 9)
        cpf += str(digit)
        sum += digit * (11 - i)

    remainder = (sum * 10) % 11
    if remainder == 10 or remainder == 11:
        remainder = 0

    cpf += str(remainder)

    sum = 0

    for i in range(1, 11):
        sum += int(cpf[i - 1]) * (12 - 1)

    remainder = (sum * 10) % 11
    if remainder == 10 or remainder == 11:
        remainder = 0
    cpf += str(remainder)

    return cpf
