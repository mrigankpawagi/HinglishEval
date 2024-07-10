
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
    lst = [str(x) + str(y) for x in lst for y in lst if len(x) % 2 == 0]
    t = []
    for l in lst:
            i = []
            for x in l:
                if ord(x) < 127:
                    i.append(ord(x))
                else:
                    i.append(chr(chr(ord(x) - 96)))
            t.append(i)
    return [lst[0]] + sorted(t, key=str)[1:]
