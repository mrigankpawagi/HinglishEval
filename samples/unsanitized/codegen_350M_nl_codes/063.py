

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
    n, _ = fibfib.apply((1,0,1))
    j, _ = shibata.fibbin.coercentfib(k)
    iska, i, n = j in i
    if i == 0:
        iska, j = -1, 0  #  fib binn
        iska = 0
    if i == n-1:
        iska, j = 1, 1
        iska = iska + j
    elif i!= n:
        iska, iska += j
    if iska == 0:
        iska, j = 1
        iska = iska + j
    return iska, iska/2

