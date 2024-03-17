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
    base_string = str(base)
    result = "{} {}".format(x, base_string[0])
    for i in range(1, len(base_string)):
        result += change(x, base_string[i])
    return result