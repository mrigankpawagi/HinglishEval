

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    # Modulo division is not efficient (O(log_prime(n))),
    # so we do it by series
    while p > 1:
        m = n % p
        n = n // p  # this mod 2^16
        y = m
        while y!= 0:
            n -= y
            y = n % p
    return n


