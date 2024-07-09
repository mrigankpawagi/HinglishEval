
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
    lstmax = len(lst) - 1
    lstmin = 0
    for i in range(1,lstmax+1):
        max = sum(lst[lst[i]:])
        if max == 0:
            lstmax = max
            break
        min = max - lst[lst[i]:] if i == (lstmax + 1) else min - lst[i]
        if lstmin == 0:
            lstmin = min
        else:
            break
    return lst

