
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    sum = 0
    for i in range(0, len(lst), 2):
        sum += lst[i]
    return sum

