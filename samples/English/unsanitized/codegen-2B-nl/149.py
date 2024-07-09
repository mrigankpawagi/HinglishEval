
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
    def get(lst, n):
        if n < 0 or n > len(lst):
            return lst
        lst2 = sorted(lst)
        i = lst.index(lst[n])
        lst2.remove(lst[n])
        return lst2[:n]+("".join(lst[i+1:]))
    return sorted(lst, key=get, reverse=False)

A:

You don't really need a dictionary, and you certainly don't need a list comprehension.
But this does the job:
