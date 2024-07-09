

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
    cnt = 2
    while (n % cnt)!= 0:
        cnt += 1
    return cnt == 3

