

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
    x = 0
    y = 1
    while x!= n:
        y *= x
        x += 1
    return y


