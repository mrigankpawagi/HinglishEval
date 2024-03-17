
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
        return 0
    if n == 0:
        return 1
    return n * special_factorial(n - 1)


def factorial(n):
    """
    Factorial of a number is defined as:
    factorial(n) = n * (n-1) * (n-2) * ... * 1
    jaha n > 0

    Jaise ki:
    >>> factorial(4)
    24

    Ye function ek integer input ke roop me lega aur is integer ka factorial
    return karega.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n):
    """
    Factorial of a number is defined as:
    factorial(n) = n * (n-1) * (n-2) * ... * 1
    jaha n > 0

    Jaise ki:
    >>> factorial_iterative(4)
    24

    Ye function ek integer input ke roop me lega aur is integer ka factorial
    return karega.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Factorial of a number is defined as:
    factorial(n) = n * (n-1) * (n-2) * ... * 1
    jaha n > 0

    Jaise ki:
    >>> factorial_recursive(4)
    24

    Ye function ek integer input ke roop me lega aur is integer ka factorial
    return karega.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative_2(n):
    """
    Factorial of a number is defined as:
    factorial(n) = n * (n-1) * (