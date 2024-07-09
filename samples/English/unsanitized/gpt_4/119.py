def match_parens(lst):
    str1, str2 = lst
    if str1.count('(') + str2.count('(') != str1.count(')') + str2.count(')'):
        return 'No'
    if str1.count(')') > str2.count('(') and str2.count(')') > str1.count('('):
        return 'No'
    return 'Yes'