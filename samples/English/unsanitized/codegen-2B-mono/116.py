
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
    sort_list = list(arr)
    
    for i in range(len(arr)):
        binary_one_count = bin(arr[i]).count('1')
        sort_list.append(binary_one_count)
        arr[i] = binary_one_count
    
    binary_two_count = 0
    sort_list.append(binary_two_count)
    arr[-1] = binary_two_count
    return sorted(sort_list)


if __name__ == "__main__":    
    import doctest
    doctest.testmod()