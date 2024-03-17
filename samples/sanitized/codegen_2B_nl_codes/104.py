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
    if isinstance(x, (long, int)):
        return [x]
    if len(x) <= 1:
        return x
    x_sorted = sorted(x)
    # Check if len of x is odd, if it is then return list which has only even element
    # if no x_sort is less than or equal to odd:
    if (len(x) % 2) == 1:
        return [element for element in list(x_sorted) if element % 2]
    # Check if len of x is even and at least 2, and if it is if it also odd; if not then return list having even element
    if len(x) >= 2 and len(x_sorted) >= 2:
        return [element for element in list(x_sorted) if element % 2 == 1]
    # return list of even number if len(x)%2 else list having only even element
    return [element for element in list(x_sorted) if element % 2 == 1]