from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    try:
        nums = [str(int(i)) for i in numbers.split()]
        num_dict = {}
        for i in range(10):
            num_dict[nums[0]] = nums
            nums.pop(0)
        return''.join([nums[0] for k2, nums in sorted(num_dict.items(), key=lambda kv: kv[0])])
    except ValueError as vex:
        print(vex)


