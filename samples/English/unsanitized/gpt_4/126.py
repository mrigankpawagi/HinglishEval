def is_sorted(lst):
    if len(lst) != len(set(lst)):
        return False
    return lst == sorted(lst)