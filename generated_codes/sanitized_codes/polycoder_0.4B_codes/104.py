
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

    def map(f):
        return list(set([f(k) for k in x] + [''))

    if len(x) == 0:
        return [None] * len(f)

    k1 = unique_digits([x[i]])
    k2 = unique_digits(x[k - 1])
    return map(f-x[i], map(f, [k1, k2]))

