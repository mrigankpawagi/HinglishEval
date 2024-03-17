def fib(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    def fib_rec(n):
        if n == 1:
            return 2
        else:
            return fib_rec(n - 1) + fib_rec(n - 2)
    return fib_rec(n) + n * 10