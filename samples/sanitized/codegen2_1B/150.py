
def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.
    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    if x ^ y == n:
        print(f'{xory(n, y, x)}^y == {n})
    else:
        print(f'Udaharan: {xory(n, y, n)}^y == {x}{n}')