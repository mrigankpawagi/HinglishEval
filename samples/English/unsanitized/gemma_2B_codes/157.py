
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
    # code goes here
    s = sum([a,b,c])
    print(s)
    if s >= a**2 + b**2:
        return True
    else:
        return False
'''
Test Cases:
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(1, 2, 3) == False
'''
def main():
    a, b, c = [int(x) for x in input().split()]
    print(right_angle_triangle(a, b, c))


if __name__ == '__main__':
    main()
