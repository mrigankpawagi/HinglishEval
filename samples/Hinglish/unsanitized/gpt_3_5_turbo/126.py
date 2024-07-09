def is_sorted(lst):
    return lst == sorted(lst) and len(set(lst)) == len(lst)