def add(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    new_int = -(2 ** (x - y))
    while x != 0 and y != 0:
        new_int = (new_int * x + y) % 1
        x, y = new_int
