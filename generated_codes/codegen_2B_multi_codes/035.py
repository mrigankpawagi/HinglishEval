

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    i = len(l)
    maximum = l[0]

    while True:

        if i > 0:
            i -= 1
            if l[i] < maximum:
                maximum = l[i]
            elif l[i] > l[i-1]:
                maximum = l[i-1]
            if maximum == l[i]:
                del l[i]
                i -= 1

                if l:
                    return maximum

        else:
            return maximum

