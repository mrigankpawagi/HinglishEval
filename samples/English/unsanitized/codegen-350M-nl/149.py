
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
    def __main__(argv):
        for _ in range(argv.len//2):
            lst = list_as_list(lst)
            # delete these
            #
            lst.sort_by(lambda x: math.ceil(x[0]/100))

            # this can always be done, because we have sorted_by(...)
            #  - this has the benefit of also doing sorting by order
            # and so does sort by length
            #
            lst[0] = None
            lst[1] = None
            lst[2] = None
            lst[3] =