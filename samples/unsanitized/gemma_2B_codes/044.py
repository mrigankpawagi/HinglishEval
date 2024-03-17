

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


def is_prime(n: int):
    """
    Input number n ka prime check karo.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    True
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    >>> is_prime(15)
    True
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    >>> is_prime(21)
    True
    >>> is_prime(22)
    False
    >>> is_prime(23)
    True
    >>> is_prime(24)
    False
    >>> is_prime(25)
    True
    >>> is_prime(26)
    False
    >>> is_prime(27)
    True
    >>> is_prime(2