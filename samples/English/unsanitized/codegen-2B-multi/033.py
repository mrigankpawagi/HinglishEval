

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    new_l = []
    for i in range(len(l)):
        if i%3!= 0:
            new_l.append(l[i])
    new_l = sort_second(new_l)
    return new_l


# test for sort_third func
l = [1, 7, 3, 1, 2, 1, 6, 4, 3, 1, 6, 9, 6, 9, 9, 1]
l = sort_third(l)
l2 = [1, 2, 3, 4, 6, 6, 6, 9, 9]
l3 = [1, 2, 3]
