

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 10:
        return str(x)
    elif base < 16:
        # to handle base 16
        ret = "0{}{}".format(base / 2, 2 * base - base / 2)
        ret *= int(x)
        return int(ret)
    # now base is 16
    ret = "00{}{}".format(base // 2, 2 * base - base // 2)
    ret *= int(x)
    return "{}{}".format(int(ret) // base, int(ret) % base)


