
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    accum = 0
    for i in range(1, len(lst)):
        accum += int(lst[-i])
    return accum

