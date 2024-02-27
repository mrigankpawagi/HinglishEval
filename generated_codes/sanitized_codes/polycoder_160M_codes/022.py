from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # TODO(gongshu): make a shorter list than needed
    i = 0
    # sort by value, the length of array is also the number of characters
    for value in values:
        if i >= len(value):
            break
        i = i + 1

    return filter(value, (i,))
