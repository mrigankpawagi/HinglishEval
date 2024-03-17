def triangle_area(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar teeno sides ek valid trikon banate hain to trikon ka area 2 decimal points tak round off karke return karo.
    Anyatha -1 return karo.
    Teen sides tabhi ek valid trikon banati hain jab kisi bhi do sides ka yog teesri side se adhik hota hai.
    Udaharan:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    if (a == 1) or (b == 1) or (c == 1):
        return 0
    a_a = a / (a - b - c)
    b_b = b / (b - c)
    c_c = c / (c - a)
    a_b = a_b * b_b * c_c
    a_c = a_c * c_c * b_b
    return a_c + a_b + b_a