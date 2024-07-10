

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    maxium = l[0]
    for i in l:
        if i > maxium:
            maxium = i
    return maxium

def multiply_list(l: list):
    """Multiply the elements of the list.
    >>> multiply_list([1, 2, 3])
    6
    >>> multiply_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    3
    """
    total = 1
    for i in l:
        total *= i
    return total

def odd_index(l: list):
    """Return all odd-indexed elements in the list.
    >>> odd_index([0.5, 2, 3.14, -2e10])
    [3.14, -2e10]
    >>> odd_index([0.3, -5, 2.1, -10000, 1])
    [2.1, -10000, 1]
    >>> odd_index([])
    []
    """
    odd_l = []
    for i in l:
        if (i % 2) == 1:
            odd_l.append(i)
    return odd_l


l = [4.1, 12, 5, 36.1]

def filter_positive(l: list):
    """Filter positive elements in the list.
    >>> filter_positive([3, 6, 7, -25, -2e10])
    [-2e10, 3, 6]
    >>> filter_positive([0, -2, -45, 2, -31n, -10000])
    [0, 1, 2, -31n, -10000]
    """
    positivity_sum = 0
    lst = []
    for i in l:
        if i > 0:
            positivity_sum += i
    for i in l:
        if i > 0:
            lst.append(i)
    return lst

print("The