

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
    # Check for monotonic increasing sequence -> False
    if len(l) < 2:
        return False

    diff = l[1] - l[0]
    for i in range(2, len(l)):
        if diff * (l[i] - l[i - 1]) < 0:
            return False
