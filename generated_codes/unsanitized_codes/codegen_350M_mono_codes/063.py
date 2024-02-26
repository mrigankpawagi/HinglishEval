

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
    if n <= 0:
        return 0
    # if n==1 :
    #     return 0
    if n == 2:
        return 1
    # if n==3:
    #     return 1
    maxval = 2
    minval = 1
    sum = 0
    # if n<maxval :
    #     n=n+2
    # elif n<minval:
    #     n=n-1
    for i in range(4, n+1):
        sum = sum + fibfib(n-2) + fibfib(n-3)
    return int(sum)


