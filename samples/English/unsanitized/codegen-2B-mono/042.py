

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # 1) Return list with incremented elements by 1
    # 2) Create list that would have its elements in an increasing order
    #    starting from number 1

    incr_list_ = []
    prev_x = x = 0

    while x < len(l):
        x += 1
        l[prev_x] += 1
        prev_x = x
        incr_list_.append(l[prev_x - 1])

    print(incr_list_)
    return incr_list_

## 4)  def print_max(l):
##        """
##        Return max element
##        >>> print_max([1, 2, -3, 4, 5])
##        5
##        >>> print_max([-3, 4, 5])
##        5
##        """
##        # 1) Return maximum value
##        max_val = 5
##
##
##
