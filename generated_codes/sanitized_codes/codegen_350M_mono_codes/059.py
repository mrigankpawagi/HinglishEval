def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    f = 0
    i = 1
    num = n
    while f <= i:
        while i <= num:
            print(i)
            if num % i == 0:
                f = i
            else:
                f += 1
            i += 1
        else:
            return i