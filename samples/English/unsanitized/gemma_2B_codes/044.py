

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
    if base == 10:
        return str(x)

    result = ""
    remainder = x

    while remainder > 0:
        base_rem = remainder % base
        result = result + str(base_rem)
        remainder = (remainder - base_rem) // base
    if base <= 10 and remainder < base:
        result = result + str(base - remainder)

    return result
