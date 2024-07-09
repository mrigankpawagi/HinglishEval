

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if a < 2 or a > (n ** (1.0 / 3)):
        raise TriangleException("invalid parameter")
    return a * (a + h) / 2
