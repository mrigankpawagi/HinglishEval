def unique_digits(x):
    """
    Diye gaye positive integers ki list x me Woh saare elements ki sorted list return karo jisme koi bhi even digit nahi hai.
    Dhyan de: Return ki gayi list ko increasing order me sort kiya jana chahiye.
    Jaise ki:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    return sorted([num for num in x if all(int(digit) % 2 != 0 for digit in str(num))])
