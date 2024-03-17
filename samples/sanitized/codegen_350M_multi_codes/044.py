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
    if x == 0:
        return "0"
    num = "{}".format(x - 1)
    while True:
        num += "0{}".format(base - 1 if num.isdigit() else "0")
        if num[-1] == "0":
            break
    return num