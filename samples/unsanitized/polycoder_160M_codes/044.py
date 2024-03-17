

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
    if (x!= x) or (x > 10) or (x > 11) or (x > 12):
        x /= base
    if x <= 10:
        return x
    return int(5**(int(x%10) + base))
