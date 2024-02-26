def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]