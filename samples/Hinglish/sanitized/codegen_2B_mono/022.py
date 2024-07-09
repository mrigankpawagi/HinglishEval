from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # return values
    # values
    return [int(value) for value in values if type(value) == int]