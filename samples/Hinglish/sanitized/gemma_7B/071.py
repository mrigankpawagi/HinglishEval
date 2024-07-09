
def triangle_area(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar teeno sides ek valid trikon banate hain to trikon ka area 2 decimal points tak round off karke return karo.
    Anyatha -1 return karo.
    Teen sides tabhi ek valid trikon banati hain jab kisi bhi do sides ka yog teesri side se adhik hota hai.
    Udaharan:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return round(s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
