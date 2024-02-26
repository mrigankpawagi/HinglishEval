
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
    if len(array) == 0:
        return []

    max_so_far = array[0]
    sorted_array = []

    for index in range(len(array)):
        current_sum = max_so_far + array[index]

        # this is why we used int division
        if index + 1 < len(array) and current_sum % 2 == 0:
            max_so_far = max(max_so_far, int(current_sum / 2))
        else:
            max_so_far = max(max_so_far, int(current_sum / 2))

        sorted_array.append(array[index])

    return sorted_array[:len(sorted_array) - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArr(3))
    print(sol.sortArr(5))
