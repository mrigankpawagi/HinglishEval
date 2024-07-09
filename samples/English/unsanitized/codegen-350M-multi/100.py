
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # 1. Create an empty pile
    pile = []
    while len(pile) < n + 1: # 1.1 Create the pile
        pile.insert(0, 0) # 1.2 Insert 0 in the first level
        for i in range(1, n) : # 1.3 Insert next number in the next level

            pile[i] += pile[i - 1] #
    return pile


# 10. Make an array of a size n (size <= 2) by repeatedly adding n numbers to the left
