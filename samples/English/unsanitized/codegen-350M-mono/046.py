

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
    # if n == 0: return 0
    # if n == 1: return 1
    # if n == 2: return 0
    # f = fib4(n-1)
    # g = fib4(n-2)
    # g = g+f
    # return g
    if n == 0:
        f = 0
        return f
    if n == 1:
        f = 1
        return f
    elif n == 2:
        f = 0
        return f
    else:
        f = fib4(n-1)
        g = fib4(n-2)
        return f+g + fib4(n-3)
        

print(fib4(5))
