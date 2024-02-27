
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
    # https://github.com/python/cpython/blob/3.4/Lib/intobject.c#L36
    if n < 0:
        return 0
    # https://github.com/python/cpython/blob/3.4/Lib/intobject.c#L69
    if n < 1:
        return 1
    # https://github.com/python/cpython/blob/3.4/Lib/intobject.c#L72
    return n * special_factorial(n - 1)

