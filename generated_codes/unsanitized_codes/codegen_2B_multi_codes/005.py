from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    i = 0
    res = [delimeter]
    while i < len(numbers):
        res.append(numbers[i])
        i += 1
        if i < len(numbers):
            res.append(numbers[i])
        i += 1
    return res


if __name__ == '__main__':
    print(intersperse([-1, -1, -1, -1,-1], -1))
    print(intersperse([5, 4, 3, 2, 1], 4))
    print(intersperse([], 4))
