

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n <= 1:
        return 0
    elif n == 2:
        return fib1(1)
    elif n >= 3:
        fib3 = fib3_rec(fib4(n-1), fib4(n-2), fib4(n-3))
        return fib3
    elif n > 0 and n < 2:
        return fib2(n-1) + fib1(n-2) + fib1(n-3)
    else:
        return fib3(n-1) + fib1(n-2) + fib1(n-3) + fib2(n-4) + fib1(n-5) + fib3(n-6) + fib5(n-7)

for i in range(nfib(1000)):
    c = fib4(i)

    print(i, c)

print(f'fib4(1)')