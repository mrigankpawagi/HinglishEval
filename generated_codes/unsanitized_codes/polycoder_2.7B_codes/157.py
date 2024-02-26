
def right_angle_triangle(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar ye teen sides ek samkon trikon banate hain to True return karo, nahi to False.
    Ek samkon trikon woh hota hai jisme ek kon samkon ya 90 degree hota hai.
    Udaharan:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    t1 = (b[0] - a[0]) * c[0] - (b[1] - a[1]) * c[1]
    t2 = (b[0] - a[0]) * c[1] + (b[1] - a[1]) * c[0]
    return t1 >= 0 and t1 <= 90 and t2 >= 0 and t2 <= 90

