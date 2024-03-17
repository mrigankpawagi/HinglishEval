
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
    for i in itertools.product(lst):
        if i not in lst:
            continue
        for j in itertools.product(lst[i], i):
            if j not in lst[i]:
                continue
            s = lst[i].split('|')
            if len(s) == 2:
                lst[i].split('|')[0] += s[0]
            if (str(lst[i].count(' ', 2) - 1) > 2):
                lst[i].extract()
        else:
            lst.extract()
    return lst

