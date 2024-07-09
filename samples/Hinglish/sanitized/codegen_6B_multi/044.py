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
    if x < 0:
        sign = "-"
        x = abs(x)
    else:
        sign = ""
    bits = []
    while x:
        bits.append(x % base)
        x = x // base
    bits.reverse()
    return sign + "".join(map(str, bits))