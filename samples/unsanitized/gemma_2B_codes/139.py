def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    jaha n > 0

    Jaise ki:
    >>> special_factorial(4)
    288

    Ye function ek integer input ke roop me lega aur is integer ka special
    factorial return karega.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * special_factorial(n - 1)


def special_factorial_iterative(n):
    """
    Iterative version of special_factorial.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    if n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def special_factorial_recursive(n):
    """
    Recursive version of special_factorial.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * special_factorial_recursive(n - 1)


def special_factorial_iterative_recursive(n):
    """
    Iterative version of special_factorial_recursive.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    if n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def special_factorial_iterative_recursive_memoization(n):
    """
    Iterative version of special_factorial_recursive_memoization.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    if n == 1:
        return 1
    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 1
        if n == 1:
            return 1
