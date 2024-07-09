
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
    if n % 2 is 0:  # when n is odd, the next level of stones is only one stone.
        l = n          # so first element will be n
    else:
        l = 2 * n      # so first element will be 2 * n
    return [l]


