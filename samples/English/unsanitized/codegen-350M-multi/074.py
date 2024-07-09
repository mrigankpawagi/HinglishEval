
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
    try:
        c1, c2 = count_in_sorted(lst1)
        if c1 > 0 and c2[0] == c1 and len(lst1) <= len(lst2) - c1:
            return [lst2]
        c2, c1 = count_in_sorted(lst2)
        if c1 > 0 and c2[0] == c1 and len(lst1) <= len(lst2) - c1:
            return [lst1]
    except:
        pass
    return lst2

	
