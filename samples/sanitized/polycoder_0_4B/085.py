def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    e = defaultdict(int)
    try:
        for it in lst[1::2]:
            e[str(it)] = True
        for it in lst[2::3]:
            e[str(it)] = False
        return e
    except Exception as e:
        if e.args[0] == 2:
            return [0]
        elif e.args[0] == 4:
            return [1]
        elif e.args[0] == 2:
            return [2]
        elif e.args[0] == 3:
            return [8]
        elif e.args[0] == 6:
            return [0]
        elif e.args[0] == 7:
            return [1]
        else:
            return [0.5]
