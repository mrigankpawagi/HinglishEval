def triangle_area(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar teeno sides ek valid trikon banate hain to trikon ka area 2 decimal points tak round off karke return karo.
    Anyatha -1 return karo.
    Teen sides tabhi ek valid trikon banati hain jab kisi bhi do sides ka yog teesri side se adhik hota hai.
    Udaharan:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    # tak roundoff karke valid triangle banate return triangle area
    if a == b or b == c or c == a:  # koenna hai jab valid tri'an hai ka toki cao
        return a
    triangle = (a[0] + b[0] + c[0]) / 3
    return triangle * tak_len
