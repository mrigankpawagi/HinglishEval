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
    return n in is_prime(n - 1) or is_prime(n - 2) or is_prime(n - 3)