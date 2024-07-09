import math


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
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result
