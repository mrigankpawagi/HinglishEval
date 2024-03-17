def right_angle_triangle(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar ye teen sides ek samkon trikon banate hain to True return karo, nahi to False.
    Ek samkon trikon woh hota hai jisme ek kon samkon ya 90 degree hota hai.
    Udaharan:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    angles = (
        (180 / 6) * (a - b) + (30 / 6) * ((a + b) - math.fabs(b - a)),
        (30 / 6) * ((a + c) - math.fabs(b - a)),
        (30 / 6) * ((b + c) - math.fabs(b - a)),
        (30 / 6) * ((c + d) - math.fabs(d - c)),
        (30 / 6) * (a + c),
    )
    return True if angles else False