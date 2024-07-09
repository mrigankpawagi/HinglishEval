

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    base = str(base)
    if base < 10:
        # integer - simple
        tmp = bin(x)[2:].lstrip("0b")
        if sum(int(tmp[2*i:i+2]) < 10 for i in range(0, len(tmp) // 2 - 1)) <= 1:
            tmp = _convert_int_to_base_plus_prefix(int(tmp), base)
        else:
            tmp = _convert_int_to_base_minus_prefix(int(tmp), base)
    else:
        # integer - complicated
        tmp = ''
        for i in range(10, base + 2):
            tmp = _convert_base_plus_prefix_to_int(tmp, i)
            if tmp:
                break
        if len(tmp)==base:
            # it is the whole thing
            return "%s0x%x" % (base, x)
        else:
            # it has fractional part of float
            return "%s%.0f" % (base, math.trunc(x))

class BaseError(ValueError):
    """BaseError is raised for base conversion errors.

    >>> BaseError("Error!")
    BaseError: Error!
    >>> from base import base
    >>> base.BaseError("Error!")
    BaseError: 'Error!'

    """
    pass

