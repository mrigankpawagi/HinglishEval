

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 2
    for i in range(2, n):
        if n % i == 0:
            return i
    return n

