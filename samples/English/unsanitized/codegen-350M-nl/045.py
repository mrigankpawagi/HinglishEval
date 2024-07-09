

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return int(atan2(2 * h, a * h))

  def draw_triangle(self, angle):
    """Given 3 angles and their corresponding sides:
    >>> triangle_triangles(6, 3, 4, 5)
    [1.5, 1.3, 1.2]
    >>> triangle_triangle(6, 3, 4, 5)
    [4.9, 4.8, 3.9]
    """
    if angle<0:
        self.triangle=Triangle(angle,0)
    else:
        self.triangle=self.triangle.sides[0]
        self.triangle.sides[1]+=2 if angle<0 else 0
        self.triangle=self.triangle
        if self.triangle is not None:
            self.triangle.set_size([2][3])
            self.triangle.set_center([1, 3])   # Make side 1 1,3 1,1
            self.triangle.set_top([[]])
            self.triangle.show()


class Triangle(object):
    '''
    Triangle has 2 elements: sides, and top, with corresponding sides and top.

    If two sides meet:
    '''
    sides=Triangle('sides')  # Sides as a 2d array
    top=Triangle('top') # top top
    self.triangle_sides((sides[0], sides[1]).sides, sides[2])    # triangle
