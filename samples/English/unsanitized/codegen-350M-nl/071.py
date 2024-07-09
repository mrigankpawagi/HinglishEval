
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
    for i in range(2, 6):
        if i<=2:
            continue
        if i == 6:
            return int(a*b) + int(c*b)
        else:
            c = 0
            for j in range(i*i): 
                c = int(0.5-b/j)*j+c
            return c
    with arcqox.errors.QuadRegionErrorInterceptor(arcqox.regions.cursor, False) as ire:
        for a, b, c in triangle_area(a, b, c):
            ire.get_value(_, is_rectangle=False)
    ire.get_region()
    return (int(a*b)*c + int(c*b)), 0
    '''
    Two sides form a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(1, 2, 5) == 7.00
    triangle_area(0, 1, 2) == -1
    '''
 