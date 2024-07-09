
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    lst = list(lst)
    ints = sum(x for x in lst if int(x) <= len(lst))
    return [int(i) for i in ints] + lst
    # pd.plotting.show(ints)
