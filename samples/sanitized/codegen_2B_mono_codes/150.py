def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.
    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    if x % 2 == 0 and y % 2 == 0:
        print(
            f"{x} is divisible by 2 and also {y} is divisbleby 2.\nEither {x} is divisible by 2 and also {y} "
            f"is divisble by 2."
        )
    elif x % 2 != 0 and y % 2 != 0:
        print(f"Both of those {x} are odd so {y} is divisble by 2.")
    else:
        print(f"{x} is odd so {y} is divisble by 2.")