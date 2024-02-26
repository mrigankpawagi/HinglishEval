
def triangle_area(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar teeno sides ek valid trikon banate hain to trikon ka area 2 decimal points tak round off karke return karo.
    Anyatha -1 return karo.
    Teen sides tabhi ek valid trikon banati hain jab kisi bhi do sides ka yog teesri side se adhik hota hai.
    Udaharan:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    area = 0
    if triangle_area(a - b, a + b, c) == -1:
        return float('inf')
    elif triangle_area(a - b, a + b, c) == triangle_area(b - a, a + b, c) + triangle_area(b - a, a + b, c) == triangle_area(a - b, a + b, c) + triangle_area(b - a, a + b, c):
        d = triangle_area(a - b, a + b, c) - triangle_area(b - a, a + b, c)
        return d + triangle_area(a - b, b + a, c)
    else:
        area = triangle_area(a - b, a + b, c)
    return area

