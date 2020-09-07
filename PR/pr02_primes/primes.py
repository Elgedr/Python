"""Primes."""
def is_prime_number(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    elif x % 1 == 0 and x % x == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    print(is_prime_number(4))
