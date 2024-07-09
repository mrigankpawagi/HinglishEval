
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    sorted_arr = []
    if not array:
        return sorted_arr

    sort_range = range(0, len(array))
    odd_sum = sum(array) % 2

    for index in sort_range:
        if odd_sum:
            sorted_arr.append(array[index])

        if not odd_sum:
            sorted_arr.append(-array[index])
        odd_sum ^= 1

    return sorted_arr
# ----------------------------------------


if __name__ == "__main__":
    # run the above cell to test your code
    # before you run the below cells, please do
    # pip install nose
    import nose
