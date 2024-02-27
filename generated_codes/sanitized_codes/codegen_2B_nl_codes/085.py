def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.
    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    m = len(lst)
    if m >= 0:
        return add(lst[::2]) + add(lst[1::2])
    else:
        return add(lst)