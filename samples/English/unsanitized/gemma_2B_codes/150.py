
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n % y == 0:
        return y
    else:
        return x  
    
    

def run():
    for n in range(50):
        x = x_or_y(n, 34, 12)
        print "for case n = ", n, "the result is: ", x


if __name__ == '__main__':
    run()
