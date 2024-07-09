

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return [x for i in range(len(l)) if i%3!= 0 ] + [i for i, x in enumerate(l) if i%3 == 0 ]

test="""
    ____ __          ____ __  ___        ___
    /  _ \ \ ____  ___/  /    /  \  __  /      ___
    ::  : :|_ _\/  \_ _ \ |  \ /\__ \ |_  \ / _`| /    \              ___________          ___
    ::  : |: | \__  /    |   \/ __| |     | | |/| |/  __ ,         .___   | /   ___|      |    |
    :: / |: | | |  |____   __|  ___ |   _  | |  /\ |/  ____|   ___/    /  _ \   / _ \/__  / ___| |
    : : |: | |  |/ /       \/    | |  | | |  | | \/  |  |     | , _ \  / _` |