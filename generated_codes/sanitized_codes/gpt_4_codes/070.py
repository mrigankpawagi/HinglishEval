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
    result = []
    while lst:
        min_val = min(lst)
        lst.remove(min_val)
        result.append(min_val)
        if lst:
            max_val = max(lst)
            lst.remove(max_val)
            result.append(max_val)
    return result
