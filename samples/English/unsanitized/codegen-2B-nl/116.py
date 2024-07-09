
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    a = sorted(arr)
    return filter(lambda x:len(long(x)) % 2!= 0, a)

# Time your implementation for example with a and b given as
# arguments.
#
# >>> import timeit
# >>> timeit.timeit(lambda:sort_array(ar), number=100)
# 8.2687263398983697
# >>> timeit.timeit(lambda:sort_array(ar), number=1000000)
# 2.1535234478001398
# >>> timeit.timeit(lambda:sort_array(ar), number=1000000000)
# 5.2326690967144034
