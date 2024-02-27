
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
    n = len(lst)

    for i in range(0, n):

        min = i
        for j in range(i, n):
            if lst[min] > lst[j]:
                min = j

        lst[i], lst[min] = lst[min], lst[i]

    return lst


if __name__ == "__main__":

    print("Example:")
    print(strange_sort_list([1, 2, 3, 4, 5, 6, 7]))
    # print(strange_sort_list([2, 5, 1, 3, 6, 7, 8, 4, 9, 10]))
    # print(strange_sort_list([3, 5, 4, 7, 10, 1, 2, 8, 6, 9]))
