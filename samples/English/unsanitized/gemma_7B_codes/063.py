

def fibfib(n: int):
    """
    FibFib number sequence ek sequence hai jo Fibbonacci sequence ke saman hai aur iska definition is prakar hai:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Kripya ek function likhe jo efficiently fibfib number sequence ka n-th element compute kare.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """

    def fib(a):
        if a == 0 or a == 1:
            return 0
        elif a == 2:
            return 1
        else:
            return fib(a - 1) + fib(a - 2) + fib(a - 3)
    
    return fib(n + 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# Problem 2.1

def fibb_better(n):
    """
    Kripya ek function likhe jo efficiently fibbonacci number sequence ka n-th element compute kare.
    >>> fibb_better(4)
    3
    >>> fibb_better(10)
    55
    """
    a = 0
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()


# Problem 2.2

def fib(n):
    """
    Kripya ek function likhe jo efficiently fibbonacci number sequence ka n-th element compute kare.
    >>> fib(4)
    3
    >>> fib(10)
    55
    """
    # If the argument is smaller than either 0 or 1, return it
    if (n < 0):
        raise ValueError
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2) + fib(n-3)

# Problem 2.3

def fib_fast(n):
    """
    Kripya ek function likhe jo efficiently fibbonacci number sequence ka n-th element compute kare.
    >>> fib_fast(4)
    3
    >>> fib_fast(10)
    55
    """
    a = 0
    b = 1
    c = n
    while c:
        a, b, c = b, a+b, c-1
    return a