

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
    result = list()
    digit_dict = {9: 'A', 8: 'B', 7: 'C', 6: 'D', 5: 'E', 4: 'F'}
    while x:
        result.append(str(x % base))
        x = x // base
    result = ''.join(result[::-1])
    return digit_dict[int(result)] if result else '0'
    


if __name__ == "__main__":
    import doctest
    doctest.testmod()

