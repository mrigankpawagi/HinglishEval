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
    if n == 2:
        return True
    if n % 2 == 0:
        p = 3
    else:
        p = 5
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True