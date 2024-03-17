Here is the Python function that completes the task:

```python
def right_angle_triangle(a, b, c):
    """
    Trikon ke teeno sides ke lengths diye gaye hain. Agar ye teen sides ek samkon trikon banate hain to True return karo, nahi to False.
    Ek samkon trikon woh hota hai jisme ek kon samkon ya 90 degree hota hai.
    Udaharan:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2
```
This function first sorts the sides of the triangle in ascending order. Then it checks if the square of the longest side (hypotenuse) is equal to the sum of the squares of the other two sides. If it is, then the triangle is a right-angled triangle, and the function returns True. Otherwise, it returns False. This is based on the Pythagorean theorem.