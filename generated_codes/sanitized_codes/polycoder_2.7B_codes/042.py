def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    if not l:  # return all list
        return l, l  # return first list
    last = l[-1]
    l.append("")
    j = 0
    for i in l:
        j += 1
        if i == last:
            l.pop()
        else:
            l.append(i)
    return j, l
