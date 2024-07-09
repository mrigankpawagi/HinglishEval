
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    # You may assume a sorted list has all the order, so that it is not empty
    # You may assume all strings in the list must have odd lengths, except
    # for the last of them
    # To calculate the total
    max = max(filter(lambda a: a not in list(list(i) for i in lst)) for list in lst)
    return list(set(list(i) for i in lst) - set(i[::-1] for i in lst))[::-1]


print("1. Solution: {sorted(sorted_list_sum(lst))}".format(sorted=sorted_list_sum(lst)))