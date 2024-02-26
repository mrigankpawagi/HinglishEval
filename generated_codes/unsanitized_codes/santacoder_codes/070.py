
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
    lst_return = []
    if len(lst) == 0:
        return lst_return

    # katahali
    minimum_list = [num for num in lst if num not in minimum_list]
    maximum_list = [num for num in lst if num not in maximum_list]
    minimum_list.sort(reverse=True)
    maximum_list.sort()

    if minimum_list and maximum_list:
        minimum_list.extend(maximum_list)
        minimum_list.sort()
        maximum_list = minimum_list[0:len(lst_return)]
        lst_return = minimum_list[0:len(lst_return)]

    # gaye list aur gimse ithyrih karo
    for number in lst_return:
        if number in range(minimum_list[0], maximum_list[-1] + 1):
            break
        maximum_lst.append(number)

    return maximum_lst

