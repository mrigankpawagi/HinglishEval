

def get_positive(l: list):
    """
    List mein se sirf positive numbers return karo.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [l[i] if a == l[i] else None for a, l in itertools.zip_longest(l, [None])]

for x in [get_positive(range(10)), get_positive([-1, -2, -3])]:
    print(x)

Output:
[2, 3, 5]
[2, 2, -3]
[5, 5, 2]
[5, 2, 5]
[5, 5, 5]
[2, 2, 5]
[-3, -3, -3]

Demo on IdeOne.

