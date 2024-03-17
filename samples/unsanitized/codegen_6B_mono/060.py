

def sum_to_n(n: int):
    """
    sum_to_n ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    k = 0
    i = 1
    while (k <= n):
        k = i
        i += 1
    print(k)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
