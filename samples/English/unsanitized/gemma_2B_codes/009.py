from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    current_maxes = [numbers[0]]
    rolling_maxs = [current_maxes]
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            current_maxes.append(numbers[i])
        else:
            current_maxes = current_maxes[:-1]
            current_maxes.append(numbers[i])
        rolling_maxs.append(current_maxes)
    return rolling_maxs


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    def test_passing_tests():
        print('Success: ', doctest.testmod())

    test_passing_tests()
