
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    while True:
        if len(lst) % 2 == 0:
            lst.append((lst[-1] + lst[0]))
        else:
            lst[-1] += lst[0]
        if lst[-1] % 2 == 1: # Only odd
            return
        else:
            lst = lst[0:-1]


