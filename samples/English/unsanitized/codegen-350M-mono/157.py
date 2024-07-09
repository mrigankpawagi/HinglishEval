
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
    x1 = (-1 / 2) * b + (1 / 2) * c
    x2 = (-1 / 2) * a + (1 / 2) * c
    x3 = (-1 / 2) * a + (1 / 2) * c

    if (x1 ** 2 + x2 ** 2 + x3 ** 2) == 1:
        return True
    return False

