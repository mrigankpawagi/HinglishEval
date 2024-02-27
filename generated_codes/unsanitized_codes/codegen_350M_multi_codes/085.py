
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    n = len(lst)
    if n == 0:
        lst.append(None)
        lst.append(None)
        return lst
    elif n == 1:
        lst[0] = lst[0] + lst[1]
        lst[1] = None
        return lst
    elif n == 2:
        if lst[1] == None:
            lst[1] = lst[0] + lst[2]
        elif lst[0] == None:
            lst[0] = lst[1] + lst[2]
        else:
            lst[0] = lst[1] + lst[2]
        return lst
    elif n > 3 and n <= 6:
        if lst[0] == None:
            lst[0] = lst[1] + lst[2]
        elif lst[1] == None:
            lst[1] = lst[2] + lst[3]
        elif lst[2] == None:
            lst[2] = lst[3] + lst[4]
        elif lst[3] == None:
            lst[3] = lst[4] + lst[5]
        return lst
    else:
        print('Error! Invalid input!')  

lst = [1, 3, 2]

add(lst)
"""
# [0, 2, 3] -> [0, 2, 3, 1]
# [2, 4, 6] -> [2,4,6,1]

# [2, 4] -> [0, 4]

"""