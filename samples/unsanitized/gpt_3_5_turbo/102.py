```python
def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the largest even integer
    that is in the range [x, y] inclusive. If there is no such number, the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    largest_even = -1
    for num in range(x, y+1):
        if num % 2 == 0 and num > largest_even:
            largest_even = num
    return largest_even
```