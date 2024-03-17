
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """    sum_ = 0
    counter = 0
    return_list = []
    for i in lst:
        if i % 2 == 1:
            return_list.append(i + sum_)
        else:
            return_list.append(i)
            sum_ += i
    return return_list
