

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
    a, b, c = [0, 0, 1]
    curIndex = 0                         # Index where to start counting
    a = a + b                            # b is defined as 1
    print(f'fibfib: {n:3}', end=" ")     # Display the first number
    if curIndex == n - 1:
        print(f'fibfib: {a}', end=" ")
    else:
        a = a + b                        # a is defined as 2
        print(f'fibfib: {a}', end=" ")

    while True:                          # Keep recursion on fib(n)
        curIndex = (b + c) + c          