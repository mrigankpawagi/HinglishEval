def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    try:
        if a > b:
            return greatest_common_divisor(b, a % b)
        else:
            return a
    except:
        raise ValueError("Can't do gcd on integer arguments, are you sure you've got 0")