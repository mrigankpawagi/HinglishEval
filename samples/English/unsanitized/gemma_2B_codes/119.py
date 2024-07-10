
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    def is_open(char):
        return char in '(' or char in ')'
    def remove(string):
        return list(string)[:-1] if string[-1] != ' )') else string[:-1]
    for a in range(len(lst[0])):
        for b in range(len(lst[1])):
            if is_open(lst[0][a]) and is_open(lst[1][b]):
                if (lst[0][a] == '(' and is_open(lst[1][b])) or \
                        (lst[1][b] == '(' and is_open(lst[0][a])) \
                        or (lst[0][a] == ')' and lst[1][b] == '('):
                    a_index = a
                    while (is_open(lst[0][a_index]) and is_open(lst[1][b_])) \
                            and (a_index < len(lst[0])):
                        a_index += 1
                    b_index = b
                    while (is_open(lst[0][a_index]) and is_open(lst[1][b_])) \
                            and (b_index < len(lst[1])):
                        b_index += 1
                    return True
            elif (is_open(lst[0][a]) and not is_open(lst[1][b])) or \
                    (is_open(lst[1][b]) and not is_open(lst[0][a])):
                if remove(lst[1]) not in is_close(lst[0]) + \
                        is_open(lst[0]) + remove(lst[1]):
                    return "No"
            elif not is_open(lst[0][a]) or not is_open(lst[1][b]):
                del lst[0][a], lst[1][b]

    return "Yes"


def is_close(lst):
    '''
    You are given a sequence of strings, check if it is possible to concatenate
    every pairs of strings. In other words, if all of the strings must match
    with each other, return 'Yes', otherwise, 'No'.
    Examples:
    is_close(['(a', ' )') ==