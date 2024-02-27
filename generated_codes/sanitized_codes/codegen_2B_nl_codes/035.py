

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = len(l)
    n = 0.0
    while n < m:
        if n > len(l):
            break
        if l[n] > n:
            n += 1
        elif l[n] < n - 1:
            n -= 1
        else:
            return l[n]
        n += 1
    return n
