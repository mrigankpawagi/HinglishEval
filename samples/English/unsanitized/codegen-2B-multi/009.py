from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    new_list = numbers[:]
    while len(new_list) > 1:
        max_item = max(new_list)
        idx = -1
        for i in range(len(new_list)):
            if new_list[i] < max_item:
                idx = i
                new_list[i] = max_item
            elif -i > len(new_list)+1:
                break
        new_list = new_list[idx+1:]
    return new_list
