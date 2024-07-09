from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_list = []
    new_list.append(numbers.pop(0))
    for i in range(len(numbers)):
        if not numbers:
            break
        if i % 2 == 0:
            new_list.append(delimeter)
        new_list.append(numbers.pop(0))
    return new_list


if __name__ == "__main__":

    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
