

def add(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    num = x + y
    res = num % 2
    if res == 0:
        return num // 2
    else:
        return res

