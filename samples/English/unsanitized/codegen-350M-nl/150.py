
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # We check if n == 9
    if n in [2, 4, 6] and x in [1, 6] and y in [1] and n%2 == 0:
        x, y = x/y, y/x
    if n**2 == 0:
        return '1'
    return x

