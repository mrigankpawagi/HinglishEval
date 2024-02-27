def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        return n
    elif pow(n, 3, 1) == 1:
        return n
    else:
        return largest_prime_factor(pow(n, 2, 1)) * largest_prime_factor(pow(n, 3, 1))