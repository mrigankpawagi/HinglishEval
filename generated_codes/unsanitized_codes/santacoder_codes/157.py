
def right_angle_triangle(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar ye teen sides ek samkon trikon banate hain to True return karo, nahi to False.
    Ek samkon trikon woh hota hai jisme ek kon samkon ya 90 degree hota hai.
    Udaharan:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    triangle = False
    if ((angle(a, b, c) ** 2) + (angle(b, c, a) ** 2) >= 2 * (angle(a, b, c) ** 2) * (angle(b, c, a) ** 2)
           and (angle(a, b, c) <= 90) or (angle(c, b, a) <= 90) or (angle(b, c, a) <= 90)):
        triangle = True
        return triangle
    else:
        triangle = False
        return triangle

