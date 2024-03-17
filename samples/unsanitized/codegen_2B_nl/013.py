

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if b > a:
        return b

    while a > 0:
        a, b = b, a % a
    return b


# Python 2 Compatibility

class Number(object):
    """
    NumPy array-like object with number type.
    """
    def __array__(self):
        """
        Number array-like object with number type
        """

        return array(self, dtype = object)


class Float(Number):
    """
    NumPy array-like object with float type.

    >>> np.identity(3)
    <__main__.Float 1e+00 4e+00>
    """
    __array__ = identity


class _Float(Number):
    """
    NumPy's implementation of a float object.
    """

    __array__ = Float


class Double(_Float):
    """
    NumPy array-like object with double type.

    >>> np.identity(3.0)
    <__main__.Float 1e+00 4e+00>
    """
    __array__ = Double


class NumPyObject(object):
    """
    Use CFFI to emulate python's built-in ndarray object.
    """
    __cffi__ = False


class c_float(Float):
    """
    For float-like in a C struct.
    """