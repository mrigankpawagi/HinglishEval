
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x_smallest = x
    y_smallest = y
    
    result = -1
    while x_smallest + 1 < y_smallest:
        x_smallest = x_smallest * x_smallest
        y_smallest = y_smallest * y_smallest
        
    while x_smallest + 1 > y_smallest:
        x_smallest = x_smallest * x_smallest
        y_smallest = y_smallest * y_smallest
        
    assert x_smallest + 1 < y_smallest
    
    result = x_smallest
    
    while (1 > x_smallest * y_smallest):
        if (x_smallest % 2 == 0 and 
            x_smallest / 2 == y_smallest / 2):
            result = result * y_smallest
        # no break, else, we'll do the next pass on x_smallest
        
    return result

