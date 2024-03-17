

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)


def min_element(l: list):
    """
    List mein se minimum element return karo.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """
    return min(l)


def sum_elements(l: list):
    """
    List mein se sabke sum return karo.
    >>> sum_elements([1, 2, 3])
    6
    >>> sum_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    136
    """
    return sum(l)


def avg_elements(l: list):
    """
    List mein se sabke average return karo.
    >>> avg_elements([1, 2, 3])
    2
    >>> avg_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    12.363636363636364
    """
    return sum_elements(l) / len(l)


def count_elements(l: list):
    """
    List mein se sabke count return karo.
    >>> count_elements([1, 2, 3])
    3
    >>> count_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    11
    """
    return len(l)


def is_empty(l: list):
    """
    List empty hai ya nahi.
    >>> is_empty([])
    True
    >>> is_empty([1, 2, 3])
    False
    """
    return len(l) == 0


def is_full(l: list):
    """
    List full hai ya nahi.
    >>> is_full