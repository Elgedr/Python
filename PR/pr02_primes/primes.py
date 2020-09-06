"""Primes."""
def is_prime_number(x):
    if x/1 % 1 and x/x % x:
        return True
    else:
        return False
print(is_prime_number(2))
