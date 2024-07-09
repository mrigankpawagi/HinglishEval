def change_base(x: int, base: int):
    """
    Input number x ka numerical base, base me badal do.
    Conversion ke baad string representation return karo.
    Base numbers 10 se kam hote hain.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    res = ""
    base += 1
    for i in range(x, 100):
        if (base % 10) == 0:
            res = "0" + res
            base += 1
        elif (base % 10) == 1:
            res = "0" + res
            base += 1
        else:
            res = "1" + res
    return res
