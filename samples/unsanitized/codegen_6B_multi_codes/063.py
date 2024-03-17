

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
    fib = [None] * (n + 1)
    fib[1] = 0
    for num in range(2, n+1):
        fib[Num] = fib[Num-1] + fib[Num-2]
    return fib[n]
# fibfib(2) = 1
# fibfib(3) = 1
# fibfib(4) = 2
# fibfib(5) = 3