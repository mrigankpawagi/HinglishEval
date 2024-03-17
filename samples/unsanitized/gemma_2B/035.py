

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


def sum_of_elements(l: list):
    """
    List mein se sum of elements return karo.
    >>> sum_of_elements([1, 2, 3])
    6
    >>> sum_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return sum(l)


def product_of_elements(l: list):
    """
    List mein se product of elements return karo.
    >>> product_of_elements([1, 2, 3])
    6
    >>> product_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -120
    """
    return reduce(lambda x, y: x * y, l)


def count_of_elements(l: list):
    """
    List mein se count of elements return karo.
    >>> count_of_elements([1, 2, 3])
    3
    >>> count_of_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    10
    """
    return len(l)


def is_list_empty(l: list):
    """
    List mein se is list empty return karo.
    >>> is_list_empty([1, 2, 3])
    False
    >>> is_list_empty([])
    True
    """
    return not l


def is_list_not_empty(l: list):
    """