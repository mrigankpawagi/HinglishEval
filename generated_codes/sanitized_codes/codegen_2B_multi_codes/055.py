

def fib(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """   if n == 0 or n < 0:
        raise ValueError("Invalid input for n")
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        a = 1
        b = 1
        karo = 2
        for m in range(3, n):
            # print(m, karo)
            a, b = b, karo + a
            karo = karo + a
    # print(karo)
    return karo

