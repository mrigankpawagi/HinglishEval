
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    a = float(a)
    b = float(b)
    c = float(c)
    if a >= b and b >= c:
        return 2*(a+b+c)/3
    elif a >= c and c >= b:
        return 2*(b+c+a)/3
    elif a >= b:
        return 2*(b+c+a+b)/3
    elif a >= c:
        return 2*(a+b+c+c)/3
    else:
        return -1

