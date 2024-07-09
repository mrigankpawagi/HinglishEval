
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
    list1=[]
    
    for i in lst:
        word_len = len(i)
        if word_len%2!=0:
            word_len = word_len-1
        
        if word_len % 2 == 0:
            i = i[ :word_len] + i[word_len: ]
            print(i)
            list1.append(i)
        elif word_len % 2==1:
            lst = lst[word_len//2 +1:] + lst[:word_len//2]
    return list1

"""Problem : [1 2 2 3 3 4 4 4 5 5 5 5]
     => [1 1 1]
     => []
     => [1 2 2 2 3 3 4 4 4 4 5]
     => [1]
     => [2 2 2 1]
     => [3 3 3 3 2]
     => [4 4 4 3 4 4]
     =>[5 5 5 5 5 5 5 5 4]
     => [1 1 1 1 1 1 2 2 2 2 3]
     => [1 3 2 3 3 2 4 4 4 4 5]
     => [1 9 7 6 6 1 1 4 9 4 6]
     => [1 1 1 1 1 1 1 1 1 1 1 1 6 9]

