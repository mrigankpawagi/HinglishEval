

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
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime_iterative(n):
    """
    Agar diya gaya number prime hai to true return karo, aur anyatha false.
    >>> is_prime_iterative(6)
    False
    >>> is_prime_iterative(101)
    True
    >>> is_prime_iterative(11)
    True
    >>> is_prime_iterative(13441)
    True
    >>> is_prime_iterative(61)
    True
    >>> is_prime_iterative(4)
    False
    >>> is_prime_iterative(1)
    False
    """
    if n == 2:
        return True
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime_recursive(n):
    """
    Agar diya gaya number prime hai to true return karo, aur anyatha false.
    >>> is_prime_recursive(6)
    False
    >>> is_prime_recursive(101)
    True
    >>> is_prime_recursive(11)
    True
    >>> is_prime_recursive(13441)
    True
    >>> is_prime_recursive(61)
    True
    >>> is_prime_recursive(4)
    False
    >>> is_prime_recursive(1)
    False
    """
    if n == 2:
        return True
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    return is_prime_recursive(n - 1)

def is_prime