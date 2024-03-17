
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    total = 0
    for i in range(len(lst)):
        total += lst[i]

    add = int(total/2)
    list = []
    for i in range(0, len(lst), 2):
        list.append(lst[i])
    for j in range(1, len(lst)):
        if (j % 2!= 0):
            list.append(add)
    print(np.asarray(list))
    return list