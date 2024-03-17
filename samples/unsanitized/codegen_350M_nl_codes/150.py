
def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.

    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """

    if x <= n:
        return n

    for i in xrange(0, n):
        if x >= n:
            return n

    if x < n:
        return n

    return True

