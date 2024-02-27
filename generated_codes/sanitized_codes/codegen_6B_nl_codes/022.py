from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    val = next(itr for itr in values if isinstance(itr, int))
    if val == "a":
        return [3.14, 5]
    elif val == 3.14:
        return [3.14]
    else:
        return []