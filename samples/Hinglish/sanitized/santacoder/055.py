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
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
