
def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    jaha n > 0

    Jaise ki:
    >>> special_factorial(4)
    288

    Ye function ek integer input ke roop me lega aur is integer ka special
    factorial return karega.
    """
    assert n > 0
    import math
    return math.factorial(n) * (
        math.factorial(n - 1) * (math.factorial(n - 2))) * math.factorial(1)
