
def triangle_area(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar teeno sides ek valid trikon banate hain to trikon ka area 2 decimal points tak round off karke return karo.
    Anyatha -1 return karo.
    Teen sides tabhi ek valid trikon banati hain jab kisi bhi do sides ka yog teesri side se adhik hota hai.
    Udaharan:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    if(not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int)):
        return round(-1, 2)
    if(not(a > 0 and b > 0 and c > 0)):
        return round(-1, 2)
    if(equal(a, c)):
        return round(0, 2)
    if(equal(a, b)):
        return round(sqrt(2)*a, 2)
    ab = side_side_distance(a, b)
    ac = side_side_distance(a, c)
    bc = side_side_distance(b, c)
    p = ab*ac/(2*ab + ac + bc)
    q = ac*bc/(2*ab + ac + bc)
    r = bc*ab/(2*ab + ac + bc)
    return round(p + q - r, 2)


if __name__ == "__main__":
    print triangle_area(3, 4, 5)
    print triangle_area(1, 2, 10)
