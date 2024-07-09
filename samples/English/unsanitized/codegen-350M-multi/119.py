
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
    parens = set()
    for s in lst:
        for p in map(lambda x: x.strip(), s.split()):
            if ((p in map(lambda x: x.strip(), parens))
                    or (p in map(lambda x: x.strip(), p.upper().split()))):
                return True
            else:
                parens.add(p)
    return False

if __name__ == '__main__':
    lst = ['()()', '()()', '()()')
    print match_parens(lst)
