

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
    if n < 2:
        return False
        
    f = 5 * n + 1
    d = int(n **.5)
    f_square = f ** 2
    for i in xrange(d, n - 1, -1):
        f_square = (f * f_square) / (i - 1)
        if f_square > n:
            return False
    return True

