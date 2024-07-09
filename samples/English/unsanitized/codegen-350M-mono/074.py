
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
    new_lst = []
    for i in lst1:
        if len(i) < len(lst2):
            new_lst.append(i)
    return new_lst

# 🚨 Don't change the code above 👆

# Testing
print(total_match([], ['']))  # Should return an empty string
print(total_match([], ['a']))  # Should return an empty string
print(total_match(['hi', 'admin'], ['hi']))  # Should return ['hi']
print(total_match(['hi', 'a'], ['hi', 'a', 'hi']))  # Should return ['hi']
