def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    for i in range(len(lst) - 1):
        if lst[i] % 2 == 0:
            if lst[i + 1] % 2 != 0:
                lst.insert(i + 1, lst[i] + lst[i + 1])
    return lst
