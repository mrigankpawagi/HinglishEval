

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # formula:
    #   area = hypotenuse * (height - base) / 2
    #
    #       Area of a triangle of height h (height-h)
    #       hypotenuse
    #      --------------------------------------
    #            base
    #            height
    #
    #      (base - height) / 2
    return h * (h - a) / 2


