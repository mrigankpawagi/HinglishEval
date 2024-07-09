
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
    p = ((a+b+c)/2)   
    val1 = (((b*c)-p*a)/(c*(b-c)))**(0.5)
    val2 = (((p*b)-c*a)/(c*(b-c)))**(0.5)
    val3 = (((p*c)-b*a)/(b*(c-c)))**(0.5)
    if val1**2+val2**2+val3**2<0:
        return -1
    else:
        return round(val1*val2*val3,3)


#Test Functions
