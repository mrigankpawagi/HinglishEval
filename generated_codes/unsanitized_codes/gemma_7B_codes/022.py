from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


def filter_even_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf even integers ke liye filter karo
    >>> filter_even_integers(['a', 3.14, 5])
    []
    >>> filter_even_integers([1, 2, 3, 'abc', {}, []])
    [2]
    """
    return [value for value in values if isinstance(value, int) and value % 2 == 0]


def filter_odd_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf odd integers ke liye filter karo
    >>> filter_odd_integers(['a', 3.14, 5])
    [5]
    >>> filter_odd_integers([1, 2, 3, 'abc', {}, []])
    [1, 3]
    """
    return [value for value in values if isinstance(value, int) and value % 2 != 0]


def filter_integers_greater_than(values: List[Any], threshold: int) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    jo threshold se bada ho
    >>> filter_integers_greater_than(['a', 3.14, 5], 3)
    [5]
    >>> filter_integers_greater_than([1, 2, 3, 'abc', {}, []], 3)
    [1, 2]
    """
    return [value for value in values if isinstance(value, int) and value > threshold]


def filter_integers_less_than(values: List[Any], threshold: int) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    jo threshold se chota ho
    >>> filter_integers_less_than(['a', 3.14, 5], 3)
    [3.14]
    >>> filter_integers_less_than([1, 2, 