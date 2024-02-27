

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    print(2 ** 31 - 2)
    nk = 2 ** 31 - 1
    result = 1
    for i in range(3, nk, 2):
        if (n % i) == 0:
            result = i
    print(result)

