
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
    if x % 10 == 5 or x % 10 > 3:
        return list(str(x))
    
    for i in range(2, x+1):
        if ((x % i) == 5):
            continue
        else:
            s = list(str(i))
            n = len(s)
            for j in range(1, n, 1):
                s.insert(j,"0")
            new_str = "".join(s)
            return list(str(int(new_str)))
            break
"""
