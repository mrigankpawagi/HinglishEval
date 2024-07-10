
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

    # write your code here
    while lst:
        result.append(min(lst))
        lst.remove(min(lst))

    sort_list = sorted(result)
    final_result = []

    while sort_list:
        final_result.append(max(sort_list))
        sort_list.remove(max(sort_list))

        final_result.append(min(sort_list))
        sort_list.remove(min(sort_list))

    return final_result


my_list = [1, 2, 3, 4]
print(strange_sort_list(my_list))
