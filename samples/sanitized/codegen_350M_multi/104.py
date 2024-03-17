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
    # TODO: Add a function that can take in a list of elements
    assert isinstance(x, int) or isinstance(x, float)
    n = len(x)
    if len(x) == 0:
        return x
    if not (isinstance(x, int) or isinstance(x, float)):
        return unique_digits(x)
    if n == 32:
        # for a 32 element list return exactly the karo jiste koi bhi...
        return [(x / 2), x]
    # here the element in the sublist is a unique value of the digits, let's find the karo jiste
    v = x
    res = list()
    for i in range(n + 1):
        k = v % i
        v = v / i
        res.append(k + 1)
    return unique_digits(res)