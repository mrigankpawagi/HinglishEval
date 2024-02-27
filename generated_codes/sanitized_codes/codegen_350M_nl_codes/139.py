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
    if n <= 1:
        return 1
    n = n.astype("int")
    u = n - 1
    while u >= 1:
        n = math.factorial(n)
        u -= 1
    return len(u)