

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        return None
    max = l[0]
    for each in l:
        if max < each:
            max = each
    return max


def max_slice(l: list):
    """
    List mein se maximum sum wala slice return karo.
    >>> max_slice([1, 2, 3])
    6
    >>> max_slice([5, 3, 1, -5])
    8
    """
    res = None
    if len(l) == 0:
        return res
    l.append(0)
    j = 1
    for i in range(1, len(l)):
        if not l[i] <= 0 and res is None:
            res = l[i]
            j = i
        if l[i] > 0 and res is None:
            res = l[i]
        next_sum = l[i - 1] + l[i]
        if l[j] <= next_sum and l[i] <= l[j]:
            j = i
        if next_sum <= l[j] and l[i] <= l[j]:
            j = i
        if l[j] <= res or l[i] <= res:
            res = l[i]
    return res  # -5


def test_max_element():
    l = [1, 2, 3, 4, 5]
    assert max_element(l) == 5
    l.append(5)
    assert max_element(l) == 5

    l = [7, 7, 7]
    assert max_element(l) == 7
    l.insert(0, 7)
    assert max_element(l) == 7
    l.append(0)
    assert max_element(l) == 7
    l = []
    assert max_element(l) is None


def test_max_slice():
    print('\nStarting with slice')
    l = [5, 6, 0, 8, 55, 3]
    assert max_slice(l) == 98
