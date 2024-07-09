

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    assert isinstance(l, list), "l must be list"
    result = []
    for i in range(len(l)):
        if i % 2 == 1:
            result.append(l[i])
    return result


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import sep
        __package__ = str('.'.join(['..'] * (sep.rstrip(sys.path[0]).count(sep) - 1)))

    if __package__ is not None:
        add_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '').replace(sep, '.')
        if add_path not in sys.path:
            sys.path.insert(0, add_path)
    try:
        from.sort_util import sort
        from.sort_util import sort_even
        from.cmp import compare
        from.cmp import order
        from.cmp import swap
        from.cmp import index
        test_cmp()
        test_cmp_even()
        test_sort_even()

    except ImportError as ex:
        if str(ex).lower().find('no module names or paths')!= -1:
            print('error: couldn\'t find sort util')
        else:
            raise ex
