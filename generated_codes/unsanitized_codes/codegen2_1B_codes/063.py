

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
    if n <= 1:
        return 0

    m, n_int = divmod(n, 2)
    print(
        f'c_{n} c_{m} c_{n_int} c_{n_int + m} = fibfib(n-(m+1)) c_{m+1} c_{m}')
    return kare(n_int + m + 1)


#