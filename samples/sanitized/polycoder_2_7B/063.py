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
    import math

    if n <= 1:
        return n
    elif n == 2:
        return 0
    else:
        return round(math.factorial(n - 1) * math.factorial(n))
