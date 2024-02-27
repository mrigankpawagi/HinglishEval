

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < b:
        temp = a
        a = b 
        b = temp
    for i in range(int(a/b) + 1):
        if (a%i == 0) and (b%i == 0):
            return i

