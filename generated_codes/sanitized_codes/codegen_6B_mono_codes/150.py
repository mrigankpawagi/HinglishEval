def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.
    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    return x if n % x == 0 or n % y == 0 else y