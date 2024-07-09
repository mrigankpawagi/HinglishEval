

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 0:
        raise ValueError("Negative n not supported.")
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

