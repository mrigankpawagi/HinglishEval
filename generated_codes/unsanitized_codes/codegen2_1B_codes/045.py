

def triangle_area(a, h):
    """
    Ek side ki length aur height di gayi ho to, triangle ka area return karo.
    >>> triangle_area(5, 3)
    7.5
    """
    b = (4 * sin(a/2 * pi / 3) + sin(h / 2))/(pi * Math.sqrt(1 - a * a))
    c = (3.14159 / 2 - h) / 2
    return b*b * c


#