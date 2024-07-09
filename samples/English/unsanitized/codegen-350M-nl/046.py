

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
    n = 0
    result = 0
    while n == 0:
        yield fib4(n)
        n = n + 1

If you're trying to understand the Fibonacci Sequence, or use the Fibonacci Sequence directly, or use it with Fibonacci Polynomials, you should try it again; see also @SebastianKron, who has a good answer for all of the other questions you might have.

