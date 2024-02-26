
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == x or n == y:
            return n
    else:
        for i in range(2, int(math.log(n, 2)) + 1):
            if n % i == 0:
                p = i
                x2 = x
                y2 = y - (p ** 2) * (x ** 2)
                return x2 + y2
                break
    print(f("I got lucky!"))

