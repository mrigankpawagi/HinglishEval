def triangle_area(a, h):
    """
    Ek side ki length aur height di gayi ho to, triangle ka area return karo.
    >>> triangle_area(5, 3)
    7.5
    """
    hum = 1 / float(h)
    h = h + float(a)

    k2 = 2 * h * h
    k3 = 2 * h * h * h
    k4 = 2 * h * h + h

    return (a + h - (k1 / k2) - k3 + k4) / (k1 / (k1 + (k2 / k2)))
