
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    lst1_len = len(set(lst1))
    lst2_len = len(set(lst2))

    if lst1_len == lst2_len:
        return lst1

    # get the numbers of chars in both lists
    lst1_num = map(max, lst1, lst2)
    lst2_num = map(max, lst2, lst1)

    # get the number of chars to add to bring both lists close together
    # to the same length
    min_chars = min(float(max(lst1_len, lst2_len)) / 3, float(max(lst1_num, lst2_num)))
    lst1_num = map(lambda x: x + min_chars, lst1_num)
    lst2_num = map(lambda x: x + min_chars, lst2_num)

    # get the indices in both lists that appear more often in one list
    lst1_freq = {}
    lst2_freq = {}
    for i, x in enumerate(lst1_num):
        lst1_freq.