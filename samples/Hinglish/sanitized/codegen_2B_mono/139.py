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
    if n <= 0:
        return 1
    else:
        a = 1
        while n > 1:
            a = a * n
            n -= 1
        return a