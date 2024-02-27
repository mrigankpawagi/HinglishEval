
def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.

    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """

    while True:
        if x_or_y(n, x, y) == x or x_or_y(n, x, y) == y:
            if n == 1 or n % 2 == 0 or n == 3 or n == 5 or n == 7 or n % 2 == 1 or n == 13 or n == 17 or n == 19 or n % 2 == 2:
                print("N. {0!r} : {1!r}".format(n, x_or_y(n, x, y)))
                break
