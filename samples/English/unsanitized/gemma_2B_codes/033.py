

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_third = list(sorted(l))
    i = 0
    for m in range(0, len(l_third), 3):

        t = l_third[i:i+3] 

        if t:
            j = l_third.index(min(t))
        else:
            j = -1

        l_third[i:i+3] = l_third[j:j+3]
        l_third[j] = min(t)

    return sorted(l_third)

from doctest import testmod

if __name__ == "__main__":
    testmod()
