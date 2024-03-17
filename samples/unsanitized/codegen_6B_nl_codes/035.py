

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if l==[] or len(l)<2:
        return None
    elif len(l)==1:
        return l[0]
    elif sorted(l)==[],  (l[-2],l[-1]):
        return l[0]
    else:
        return max(l[1],max_element(l[0:2])[0])

Вывести список среди списка он самый короткий.
n - длина списка.
