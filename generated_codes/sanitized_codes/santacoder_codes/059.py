def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 0
    while n % 2 == 0 and i < 20:
        n = n / 2
        i = i + 1
    if n % 2 == 0 and i < 20:
        return 2
    for i in range(3, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            i = i + 1
            while i <= math.sqrt(n):
                if n % i == 0:
                    n = n / i
                    i = i + 1
                    if i == 4:
                        return i
    return n
