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
    result = ""
    while x > 0:
        mod = x % base
        if mod > 9:  # In base 10 thi 10 chaiye.
            # Yea bas ten paar me integer lage.
            result = str(mod) + result
        else:  # Yea bas ten paar ek print karenge.
            result = str(mod) + result
        x = x // base
    return result