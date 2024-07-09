

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
    temp = []
    while x > 0:
        d = 10**(len(str(x % base)) -1)
        r = x % base
        temp.append(str(r // 2**d))
        x = x // base
    temp.append(str(1))
    return "".join(temp)
    
