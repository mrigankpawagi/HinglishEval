
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
    """    if n <= -4 or int(n) <= 1:
        return 2
    k = 0
    while v > n:
        if v / n > 1000:
            # this formula has a lot of zeros and can fail if the number is
            # negative
            return k
        k = k + (v % n)
        v = v / n

    return k

