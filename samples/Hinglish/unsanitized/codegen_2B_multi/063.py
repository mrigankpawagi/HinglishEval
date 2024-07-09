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
    # fib number as 1
    if n > 1:
        new_fib_n = n

        if n % 2 == 0:
            # a Fibbonacci sequence with even number of elements
            return fibfib(new_fib_n - 1) + fibfib(new_fib_n - 2)

        else:
            # a Fibbonacci number with odd number of Fib number sequence
            return fibfib(new_fib_n - 1) + fibfib(new_fib_n - 2) * fibfib(new_fib_n - 3)
    else:
        # fib number at nth element
        return n
