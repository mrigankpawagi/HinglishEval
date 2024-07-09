

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n >= 2 * 2 ** n:
        return False
    x = int(x)
    if n < 2 or n % 2 < 0:
        return False
    for x in range(n-2, 0, 2*2 ** n + 1, 2**2 ** n + 2):
        if x == 0 or x % 2 == 0:
            return False
    return True

