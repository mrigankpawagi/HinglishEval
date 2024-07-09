

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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_iter(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_iter(10)
    55
    >>> fib_iter(1)
    1
    >>> fib_iter(8)
    21
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_rec(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_rec(10)
    55
    >>> fib_rec(1)
    1
    >>> fib_rec(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_rec_memo(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_rec_memo(10)
    55
    >>> fib_rec_memo(1)
    1
    >>> fib_rec_memo(8)
    21
    """
    memo = {}
    def fib_rec_memo_helper(n: int):
        if n in memo:
            return memo[n]
        if n == 0:
            memo[n] = 0
        elif n == 1:
            memo[n] = 1
        else:
            memo[n] = fib_rec_memo_helper(n - 1) + fib_rec_memo_helper(n - 2)
        return memo[n]
    return fib_rec_memo_helper(n)


def fib_rec_memo_iter(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_rec_memo_iter(10)
    55
    >>>