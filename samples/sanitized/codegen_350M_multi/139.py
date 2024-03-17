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
    if n == 0:
        return 1
    k = special_factorial(n - 1.5)
    d = special_factorial(n)
    if d > k:
        d = k
    return d