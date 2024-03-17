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
    lst_cpy = lst[:]
    for i in range(len(lst)):
        min_value = min(lst)
        max_value = max(lst)
        if min_value == max_value:
            taka = taka + 1
        else:
            lst.remove(min_value)
            lst.remove(max_value)
        lst.append(0)
    return lst