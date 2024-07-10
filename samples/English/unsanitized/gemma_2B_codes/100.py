
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
    def make_pile_by_loop(n):
        res = [n]*n
        for i in range(n):
            r = i if n&1 else i-1
            res[i] += res[r]
        return res
    def make_pile_recur(n):
        res = [x for x in range(n+1)]
        for i in range(n):
            res[i+1] += res[-1]*(n+1-i)
        return res
    def make_pile(n):
        return [make_pile_by_loop(n//2), make_pile_by_loop(n//2)]

    return make_pile(n)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from pprint import pprint as pp
    a = make_a_pile(1)
    pp(a)
    a = make_a_pile(3)
    pp(a)
    a = make_a_pile(5)
    pp(a)
