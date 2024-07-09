
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
    if arity(arr)!= 0:
        return None 
    signs = [1, -1, 0] * len(arr)
    for i, i1 in enumerate(arr):
        i, i11 = divmod(i1, 2)
        signs[i] = -int(i11) if i1!= 0 else 0
    return signs


assert prod_signs([-1, 0]) == 0
assert prod_signs([-2, 0]) == 0
assert prod_signs([-2, -1, 1]) == 0
assert prod_signs([-1, -1, 0]) == None
assert prod_signs([-5, -5, -1, -1]) == None

s = [7, 13, 7, 10]

sum_signs = [1, -1, 0] for i1, i2 in enumerate(s)
print sum_signs
print sum_signs == prods_signs(s)


