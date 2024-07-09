

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n < 2:
        return 0
    elif n < 4:
        return 2
    elif n < 6:
        return [2, 3]
    elif n < 16:
        return prime_fib(4)
    else:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
