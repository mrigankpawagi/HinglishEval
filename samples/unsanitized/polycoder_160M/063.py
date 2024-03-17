

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

    n = n // 2
    from sage.misc.as_sequek_tuple import as_sequek_tuple  # type: ignore

    if n == 0 or n == 1:
        return 0
    ariad = -1
    for l in range(n):
        if not (is_number(l) or is_number(l % n)):
            ariad = -1
        if fibfib(iriad)!= ariad + fibfib(1):
            ariad = fibfib(iriad)
        if fibfib(0)!= ariad + fibfib(1):
            ariad = fibfib(0)
        yield ariad
    if ariad + fibfib(1)!= -1:
        yield ariad + fibfib(2)

