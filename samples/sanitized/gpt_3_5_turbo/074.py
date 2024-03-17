def total_match(lst1, lst2):
    if len(lst1) == len(lst2):
        return lst1
    elif len(lst1) < len(lst2):
        return lst1
    else:
        return lst2
