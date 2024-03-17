
def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.

    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    n = n.to_string(3, "B", n.__repr__)
    if x % 2 == 0:
        return n + "." + y + "." + n
    elif n.startswith(("0","1")) or n.startswith(("1","6")) or n.startswith(("2","5")) or n.startswith(("3","4")) or n.startswith(("4","7")):
        return n + "." + 1 + "."
    elif n.startswith(("10","4")) or n.startswith(("10","12")) or n.startswith(("11","3")) or n.startswith(("11","8")) or n.startswith(("12","2")) or n.startswith(("12","4")):
        return n + "." + 2 + "." + 1 + n
    elif n.startswith(("5","4")) or n.startswith(("5","14")) or n.startswith(("14","4")) or n.startswith(("15","0")) or n.startswith(("16","2")) or n.startswith(("17","6")):
        return n + "." + x + "." + y
    elif n.startswith(("13","6")) or n.startswith(("13","16")) or n.startswith(("14","7")) or n.startswith(("15","1"))) or n.startswith(("3","6")) or n.startswith(("6","12")) or n.startswith(("3","10")) or n.startswith(("6","5")) or n.startswith(("12","5")) or n.startswith(("13","19")):
        # hone par ke par
        return n + "." + y + "." + n
    else