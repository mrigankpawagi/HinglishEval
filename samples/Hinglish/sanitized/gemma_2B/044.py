

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
    if base < 10:
        raise ValueError("Base number should be greater than 10")
    if base > 36:
        raise ValueError("Base number should be less than 36")
    if base == 10:
        return str(x)
    if base == 2:
        return bin(x)[2:]
    if base == 8:
        return oct(x)[2:]
    if base == 16:
        return hex(x)[2:]
    raise ValueError("Base number should be 10, 2, 8 or 16")

