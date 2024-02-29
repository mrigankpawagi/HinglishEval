

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
        return fib(n-1) + fib(n-2)

def fib_memo(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_memo(10)
    55
    >>> fib_memo(1)
    1
    >>> fib_memo(8)
    21
    """
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fib_memo_dict(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_memo_dict(10)
    55
    >>> fib_memo_dict(1)
    1
    >>> fib_memo_dict(8)
    21
    """
    memo = {}
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fib_memo_dict_2(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_memo_dict_2(10)
    55
    >>> fib_memo_dict_2(1)
    1
    >>> fib_memo_dict_2(8)
    21
    """
    memo = {}
    def fib_helper(n: int):
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib_helper(n-1) + fib_helper(n-2)
            return memo[n]
    return fib_helper(n)

def fib_memo_dict_3(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib_memo_dict_3(1