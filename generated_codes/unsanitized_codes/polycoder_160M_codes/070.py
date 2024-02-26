
def strange_sort_list(lst):
    """
    Diye gaye integers ki list ko, strange order mein return karo.
    Strange sorting, tab hoti hai jab aap minimum value se start karte ho,
    phir remaining integers ki maximum value, phir minimum aur aise hi aage badhte ho.

    Udaharan:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    if not isinstance(lst, (list, OrderedDict)):
        raise TypeError("lst should be a list(list) or OrderedDict(list)"
                        "or None")
    sort = sorted(lst)
    for t in sort:
        if t[0] > t[2]:
            tmin = t[1]
            tmax = t[2]
        # else: t[0] is a karo for strange sort
        if tmin > t[0]:
            tmin = 0
            tmax = len(str(sort)) - 1
        if tmax > t[1]:
            tmax = 0
            tmax = len(str(sort)) - 1
        while tmax - tmin > 0:
            sorted[tmin] = str(sort[tmin])
            sorted[tmax] = str(sort[