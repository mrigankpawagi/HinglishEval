
def right_angle_triangle(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar ye teen sides ek samkon trikon banate hain to True return karo, nahi to False.
    Ek samkon trikon woh hota hai jisme ek kon samkon ya 90 degree hota hai.
    Udaharan:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    import math
    # your code here
    return abs((math.sin((b ** 2 + c ** 2 - a ** 2)/(2 * a * c)) / sin(a * math.pi/180)) + 1) < 1

# Solution
