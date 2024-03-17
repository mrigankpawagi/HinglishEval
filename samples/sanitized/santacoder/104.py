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

    def digit(x):
        t = 0
        for i in x:
            t += i * i
        for i in range(0, len(x)):
            t -= x[i] * x[i]
        return abs(t)

    return sorted(
        list(set([digit(x[i : i + len(x)] + x[i]) for i in range(0, len(x) - 1)]))
        if len(x) > 0
        else list()
    )
