def sorted_list_sum(lst):
    lst = [i for i in lst if len(i) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst