

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) == 0:
        raise ValueError("list is empty")
    return sorted(l)[len(l)//2]

# def mymedian(l: list):
#     """Return the medians of elements in the list.
#     >>> mymedian([3, 2, 5, 4, 1])
#     [3, 2, 3]
#     """
#     if len(l) <= 1:
#         return []
#     k = len(l) // 2
#     return sorted(l)[k]

