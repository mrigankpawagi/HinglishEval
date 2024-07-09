

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0:
        return b
    if b == 0:
        return a
    # note: python chokes on a // b!!!
    # and a**b cannot be computed directly!
    # as a is int and b is int
    # so we'll use the following approach based on some recurrence relation
    # http://en.wikipedia.org/wiki/Euclidean_algorithm#Pseudocode
    assert a and b and a == int(a) and b == int(b)
    if a < 0:
        a, b = -a, -b
    while b!= 0:
        a, b = b, a % b
    return a


