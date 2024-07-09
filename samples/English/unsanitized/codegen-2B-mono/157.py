
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
    a = math.radians(a)
    b = math.radians(b)
    c = math.radians(c)
    for i in [a, b, c]:
        if math.pow(math.sin(i/2), 2) + math.cos(i) * math.cos(i + math.radians(90)) >= 0:
            return True
    return False
    
#print (right_angle_triangle(3, 4, 5))
#print (right_angle_triangle(1, 2, 3))

'''
14.
Write a function, shortest_path, 
that given a maze represented by a matrix 
where 0 = empty, 1 = wall, 2 = start, 
3 = finish 
and a start position, 
return the (row, column) of the 
position after the shortest path from an 
exceptionally long wall or the start 
to an empty position if the maze contains a start.  
If there are multiple such paths, return the smallest 
such path.
'''
