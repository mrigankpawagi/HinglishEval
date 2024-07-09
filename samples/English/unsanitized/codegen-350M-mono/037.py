

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    temp = {}
    for i, val in enumerate(l):
       temp[val] = i
    evens = []
    odds = []

    for i, val in enumerate(l):
        indexVal = temp[val]
        if i % 2 == 1:
            if odds.count(indexVal) == 0:
                evens.append(val)
            else:
                odds.append(val)
        else:
            if evens.count(indexVal) == 0:
                evens.append(val)
            else:
                odds.append(val)
    return evens, odds

# Testing sort_even
#
#     def sort_even(l: list):
#         temp = {}
#         for val in l:
#            temp[val] = l.count(val)
#         return [temp[i] for i in sorted(temp.keys())]
