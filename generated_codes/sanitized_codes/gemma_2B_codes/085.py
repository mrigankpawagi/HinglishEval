
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    if len(lst) == 0:
        return 0
    else:
        return sum(lst[i] for i in range(1, len(lst)) if i % 2 == 0)

