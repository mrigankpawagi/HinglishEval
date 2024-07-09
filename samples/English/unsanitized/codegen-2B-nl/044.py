

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
    ret = [str(x)]
    while x >= base:
        ret.append(str(x))
        x //= base
    return ''.join(ret)

print change_base(2, 8)
print change_base(10, 8)
print change_base(5, 6)
print change_base(8, 3)
print change_base(27)
