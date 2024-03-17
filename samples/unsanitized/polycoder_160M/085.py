
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    # Karo:
    for i, c in enumerate(lst):
        assert(i % 100 == 0)  # all indices in the same index i have at least 100 elements at each index
        if isinstance(c, str):
            if i == c:
                return lst
            elif i!= c:
                return [i, c]
        lst[i] = c
    # Vik:
    if len(lst) > 2:
        lst.append(2)
    return lst
