

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    pass
    """if n < 2:
        return "Not a valid number"
        # or return n == 2
    """
    for i in range(n,1,-1):
        if n % i == 0:
            return i
    """else:
        return "Not a prime"
    n**0.5
    """   


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)