

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
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_2(n):
    """
    Agar diya gaya number prime hai to true return karo, aur anyatha false.
    >>> is_prime_2(6)
    False
    >>> is_prime_2(101)
    True
    >>> is_prime_2(11)
    True
    >>> is_prime_2(13441)
    True
    >>> is_prime_2(61)
    True
    >>> is_prime_2(4)
    False
    >>> is_prime_2(1)
    False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_3(n):
    """
    Agar diya gaya number prime hai to true return karo, aur anyatha false.
    >>> is_prime_3(6)
    False
    >>> is_prime_3(101)
    True
    >>> is_prime_3(11)
    True
    >>> is_prime_3(13441)
    True
    >>> is_prime_3(61)
    True
    >>> is_prime_3(4)
    False
    >>> is_prime_3(1)
    False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_4(n):
    """
    Agar diya gaya number prime hai to true return karo, aur anyatha false.
    >>> is_prime_4(6)
    False
    >>> is_prime_4(101)
    True
    >>> is_prime_4(11)
    True
    >>> is_prime_4(13441)
    True
    >>> is_prime_4(61)