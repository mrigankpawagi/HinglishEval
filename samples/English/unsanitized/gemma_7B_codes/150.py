
def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.

    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """

    return x if is_prime(n) else y

def is_prime(n):
    """
    Ek function jo n ek prime number be hon par True return karegi, baki sab false
    """

    for i in range(2, n // 2 + 1):
         x = n%i
         if x == 0:
             return False

    return n>1


print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))
