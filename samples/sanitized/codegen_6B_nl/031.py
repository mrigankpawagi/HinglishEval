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
    if n < 2 or n == 2:
        return True
    elif n in prime:
        return False
    return all(
        n % prime[k] for k in range(len(prime)) if prime.count(n % prime[k]) == 1
    )