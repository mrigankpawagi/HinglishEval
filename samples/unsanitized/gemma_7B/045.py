def triangle_area(a, h):
    """
    Ek side ki length aur height di gayi ho to, triangle ka area return karo.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2


def triangle_perimeter(a, b, c):
    """
    Ek triangle ki 3 sides di gayi ho to, triangle ka perimeter return karo.
    >>> triangle_perimeter(5, 3, 4)
    12
    """
    return a + b + c


def triangle_type(a, b, c):
    """
    Ek triangle ki 3 sides di gayi ho to, triangle ka type return karo.
    >>> triangle_type(5, 3, 4)
    'isosceles'
    """
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


def triangle_area_and_perimeter(a, b, c):
    """
    Ek triangle ki 3 sides di gayi ho to, triangle ka area aur perimeter return karo.
    >>> triangle_area_and_perimeter(5, 3, 4)
    (7.5, 12)
    """
    return triangle_area(a, c), triangle_perimeter(a, b, c)


def triangle_area_and_type(a, b, c):
    """
    Ek triangle ki 3 sides di gayi ho to, triangle ka area aur type return karo.
    >>> triangle_area_and_type(5, 3, 4)
    (7.5, 'isosceles')
    """
    return triangle_area(a, c), triangle_type(a, b, c)


def triangle_area_and_perimeter_and_type(a, b, c):
    """
    Ek triangle ki 3 sides di gayi ho to, triangle ka area, perimeter aur type return karo.
    >>> triangle_area_and_perimeter_and_type(5, 3, 4)
    (7.5, 12, 'isosceles')
    """
    return triangle_area(a, c), triangle_perimeter(a, b, c), triangle_type(a, b, c)
