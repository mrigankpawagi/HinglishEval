def next_smallest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    if len(unique_lst) > 1:
        return unique_lst[1]
    else:
        return None