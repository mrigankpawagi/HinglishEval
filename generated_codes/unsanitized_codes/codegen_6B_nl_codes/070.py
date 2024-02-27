
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

    start = int(min(lst))
    end = int(max(lst))

    for i in range(start, end + 1):
        if lst[i] > end:
            start = i - 1
        elif lst[i] < start:
            end = i + 1
        else:
            lst[i], lst[start], lst[end] = lst[end], lst[start], lst[i]

    return lst

