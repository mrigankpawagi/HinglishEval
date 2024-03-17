def fib(n: int):
    """
    Returns the n-th Fibonacci number.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
