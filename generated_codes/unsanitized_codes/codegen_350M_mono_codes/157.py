
def right_angle_triangle(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar ye teen sides ek samkon trikon banate hain to True return karo, nahi to False.
    Ek samkon trikon woh hota hai jisme ek kon samkon ya 90 degree hota hai.
    Udaharan:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    import numpy as np
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False