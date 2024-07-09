
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
    sorted_arr = np.empty(len(arr), dtype=np.int)
    for i in range(len(arr)):
        sorted_arr[i] = arr[i]
    sorted_arr.sort(key=np.int_)
    return sorted_arr


# TODO: Remove the following function when implemented in python 3.5
#def extract_partition_array(arr, k):
#    """
#    Given an array, partitions it by comparing the number of
#    non-zero elements to the largest value of partition array
#    """
#    partition = np.array([], dtype=np.float64)
#    for i in range(len(arr)):
#        if arr[i] > 0:
#            partition += np.linspace(arr[i], 0.0, k+1).astype(np.float64)
#    return partition

