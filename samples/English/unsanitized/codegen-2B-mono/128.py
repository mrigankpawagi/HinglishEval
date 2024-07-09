
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    arr.sort()

    mags = []  # array of array of signs, with the number of signs
    # per number
    signs = []  # signs of every number

    for x in arr:
        if x!= 0:
            mags.append(signs)

        if x < 0:
            signs.append(1)  # adding sign of -1

        else:
            signs.append(0)  # adding sign of 1

    signs.append(0)

    res = 0
    for magz in mags:
        prod = 1
        for sign in magz:
            if sign == 1:
                prod *= x + 1  # adding 1 to every sign
            elif sign == -1:
                prod *= x - 1  # adding -1 to every sign
        res += prod
    return res
