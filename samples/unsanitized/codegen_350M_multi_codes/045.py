

def triangle_area(a, h):
    """
    Ek side ki length aur height di gayi ho to, triangle ka area return karo.
    >>> triangle_area(5, 3)
    7.5
    """
    x = (h - a) / 2.0
    y = (5.0 / 16.0) * pow(x, 2)
    return pi * pow(y, 2)

