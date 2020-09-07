"""Primes."""


def is_prime_number(x: int):

    """funktsioon"""
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    print(is_prime_number(121))
