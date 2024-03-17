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
    # the base case
    if n == 1:
        return 1
    elif n == 2:
        return 1
    num = fib(n - 1) + fib(n - 2)
    return num