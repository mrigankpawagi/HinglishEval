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
    # f(n-1) = f(n-1) + n * d(fib(n-1))
    return Fibonacci(fib(n - 1))