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
    strange_order = 1
    while strange_order < len(lst):
        newlist = []
        for val in lst:
            newlist += [val] * strange_order
            newlist.sort()
        strange_order += 1
        if newlist == lst:
            break
        else:
            lst = newlist
    return lst