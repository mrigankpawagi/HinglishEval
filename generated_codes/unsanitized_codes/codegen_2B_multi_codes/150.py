def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.

    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    if n > x and n > y:
        return x
    elif n < x and n < y:
        return y
    else:
        return x


# def fibonacci(n):
#     """
#     For given input n this program returns Fibonacci number
#     """
#     number1 = 1
#     number2 = 1
#     if n >= 2:
#         x = n - 2
#         number2, number1 = number2, number1 + number2
#         number2, number1 = number2, number1 + number2
#         for i in range(3, n):
#             number2, number1 = number2, number1 + number2
#         return number1
#     else:
#         return number1
