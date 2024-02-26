
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # O(n^2) time, O(n) space
    # In this case we need to add the sum of every positive array element minus the sum of every negative
    # array element.
    # TODO this is actually not what is the problem, we need to figure out which direction.
    #  i+1 instead of starting, because we want to start at the index of the 0-value, not the index
    #  of the largest number in the array.
    sub_sum = lambda arr: sum(arr >= 0) - sum(arr < 0)
    sub_sum(nums)

    return min(sub_sum(nums))


if __name__ == "__main__":
    test_cases = [
      (3, []),
      ([]),
      ([3, 2, 1], [1, 1, 1]),
      ([-4, -5, 1, 2, 3, -4, 2, 1, -6, 1], [7, -2, -4, -10, -7, -4, -6, -3, -3, -5, 4, -10])
    ]

    for test, expected in test_cases:
        print(expected)
        actual = minSubArraySum(test)
        if expected == actual:
            print("PASS")
        else:
            print("FAIL (" + str(expected) + "!= " + str(actual) + ")")
            break