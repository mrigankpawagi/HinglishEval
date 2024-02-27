

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    n = len(l)
    if n <= 1:
        return l[0]
    mid = len(l[0]) // 2
    for i in range(3, 0, -1):
        if i == 0:
            l[i:] = l[i]
        else:
            if l[i - 1] > l[i] and l[i] > l[i - 1]:
                l[i:] = max(l[i - 1], l[i])
                l[i + 1] = max(l[i], l[i - 1])
            else:
                if mid - 1 == i:
                    l[-1] = max(l[-1], l[i])
                elif (i + 1) < n:
                    l[i + 1] = max(l[i + 1], l[i])
                continue
            else:
                l[i + 1] = max(l[i + 1], l[i + 1 - mid - 1])