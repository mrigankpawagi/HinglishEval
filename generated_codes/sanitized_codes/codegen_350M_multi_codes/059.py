def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n > 1:
        primeFactorial = primeFactors[n]
        if primeFactorial == 1:
            return 1  # pometa hai.
        elif primeFactorial > 1:
            return primeFactorial