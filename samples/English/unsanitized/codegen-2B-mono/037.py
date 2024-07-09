

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    odds = []
    eve = []
    for i in range(len(l)):
        if i % 2 == 0:
            eve.append(l[i])
        elif i % 2!= 0:
            odds.append(l[i])
    even = sorted(eve, key = lambda x: x)
    eve = sorted(odds, key = lambda x: x)
    return eve + even


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print(sorted(map(int, input("Please enter the values of the list, separated by spaces: ").split()), reverse=False))
