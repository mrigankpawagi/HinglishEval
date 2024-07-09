def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        max_list.append(max_num)
    return max_list