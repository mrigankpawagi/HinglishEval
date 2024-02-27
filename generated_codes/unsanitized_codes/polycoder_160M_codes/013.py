

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if int(1 << a) >= int(1 << b) + 1:
        return int(a)
    else:
        return int(3 << a) + int(b) - 1

