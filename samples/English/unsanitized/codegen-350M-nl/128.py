
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
    sign_sum = 0
    a = (sign_sum += len(arr))
    for i, x in enumerate(arr):
        i = sign_sum * (0 if x == 0 else 1)
        j = sign_sum * (0 if x == -1 else 1)

        while i < j and sign_sum < j:
            i = sign_sum * (0 if x == 0 else 1)
            j = sign_sum * (0 if x == -1 else 1)

            a = sign_sum * (a + (j - a)) # remove extra sign

    return a * prod_signs(a)


