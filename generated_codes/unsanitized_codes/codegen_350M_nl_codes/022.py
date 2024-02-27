from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return filter_integers_by_values.copy(
        values=values,
    )
