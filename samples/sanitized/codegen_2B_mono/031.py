def is_prime(n):
    """
    Agar diya gaya number prime hai to true return karo, aur anyatha false.
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
    assert 5 > n > 0
    n = abs(n)
    if n % 2 == 0:  # n bola par
        return False
    elif n == 1:  # n bola odd
        return False
    else:
        primes = np.arange(3, n, 2)
        for p in primes:
            if n % p == 0:
                return False
    return True