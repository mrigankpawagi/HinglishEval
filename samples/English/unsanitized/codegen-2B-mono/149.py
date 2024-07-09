
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
    i=0
    n=sorted(lst)
    print(len(lst))
    s=[]
    while i<len(lst)-1:
        if len(lst[i])==len(lst[i+1]):
            s.append(tuple(lst[i]+lst[i+1]))
        i=i+2
    s=sorted(s,key= lambda i: i[0])
    s=sorted(s,key= lambda i: i[1])
    print(lst)
    return s


# def list_sort(lst):
#     return sorted(lst)

lst_test=[
    "a",
    "a",
    "aa",
    "abc",
    "abcd",
    "a",
    "d",
    "abcdefghij",
    "abc",
    "abcd"
]
for i in lst_test:
    print(i,sorted_list_sort(i))