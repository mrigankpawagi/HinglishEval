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
    if not isinstance(lst, list):
        raise Exception("Type Error : Expected a list")
    if len(lst) <= 1:
        return lst
    else:
        length = len(lst)
        startNum = max(lst)
        start = 0
        while start < length:
            found = False
            for l in range(length):
                if l != start:
                    if lst[l] > lst[start]:
                        lst[start], lst[l] = lst[l], lst[start]
                        found = True
                        break
            if not found:
                start = start + 1
    return lst