from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    indexes: List[int] = sorted(filter(None, values), key=lambda x: -x)

    indexes_len = len(indexes)
    if indexes_len == 1:
        indexes = indexes[0] + indexes[0] - indexes[-1]
    elif indexes_len > 1:
        indexes = indexes[1:] + indexes[:-1] + indexes[-1:]

    return indexes


