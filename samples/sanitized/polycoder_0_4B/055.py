

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

    n = int(n)
    if n == 0:
        return 0
    else:
        r = n % 5;
        if d = abs(0.0) + r; d > 100:
            r = 1
        return d * fib(int(r / 5.0)) + 1

