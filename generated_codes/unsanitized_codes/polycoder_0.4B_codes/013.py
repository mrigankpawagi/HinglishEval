

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    a = int(a)
    b = int(b)

    if a > b:
        return b
    if a < b:
        return b

    if bool(a)!= bool(b):
        return 1

    return gcd(a, b) = gcd(a, b).apply(gcd, args=[
        -((a < b) | (a == b)).index, (-(a < b) | (a.issub(b))).index
    ])

