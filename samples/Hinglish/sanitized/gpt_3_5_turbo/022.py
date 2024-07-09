from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    """
    return [value for value in values if isinstance(value, int)]
