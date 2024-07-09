

def monotonic(l: list):
    """
    True return karo agar list ke elements monotonically badh rahe ho ya ghat rahe ho.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if min(l) < 0: return False
    if max(l) >= l[0]: return True
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            return True
    return False
