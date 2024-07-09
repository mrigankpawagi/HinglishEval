

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return math.sqrt(h*(h - a))


if __name__ == '__main__':
    main()
