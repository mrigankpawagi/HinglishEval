

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
        return n

    middle = int(math.ceil(math.sqrt(n) + 1))
    fib = [2,3]
    factor = 0
    while len(fib) < middle + 1:
        if factor < fib[0] >= fib[1]:
            fib.insert(0, n)
            factor = n - fib[0]
        else:
            while factor >= fib[1]:
                fib.insert(0, fib[0])
                factor -= fib[1]

    return n


