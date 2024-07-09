
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    a = math.sqrt(3.) * a
    b = math.sqrt(1. + 2. * 1. / 3.) * b
    c = math.sqrt(1. + 2. * 4. / 5.) * a

    return c - b < a - b - c

