
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    result = sorted(nums, reverse=True)
    return [int(''.join(map(str, s))) for s in result]



# Your Codec
# Your code below this line is your Codec.
class Codec:

    # Return a list of all possible strings that
    # can be written the given strings
    def get_allowed_strings(self, strs):
        # Write your code here
        result = set()
        for one_str in strs:
            result.update(self.sum_digits(one_str))
        return list(result)

    # Get an integer whose digits' sum is equal to the given argument.
    def sum_digits(self, num):
        # Write your code here
        return sum(int(i) for i in str(num))
