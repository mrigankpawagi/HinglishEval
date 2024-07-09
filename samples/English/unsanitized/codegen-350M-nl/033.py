

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # We use a recursive algorithm -- a slightly more complicated one,
    # because we're going through all the "indicated" values in the list
    # we can assume they will be from divisible by three
    if len(l) < 2:
        r = sorted(l)
    elif len(l) == 2:
        for index in range(0, 3):
            l[index] = l[3 - index]
        return sort_third(l)
    else:
        r_t = l - sorted(l)
        r_t = l - [3 - i**2 for i in range(3)]
        return r_t
    return [[0, 1]] + r_t  # or [0, 1].

# Convert list elements to a sorted tuple (even if it has n - elements).
