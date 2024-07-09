
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
    if (len(lst) < 2):
        return None
    stack = []
    for strt in lst:
        if (strt == ')'):
            if (len(stack) > 0 and stack[-1] == '('):
                stack.pop()
                continue
            if(strt in stack):
                return "No"
            stack.append(strt)
        else:
            stack.append(strt)
    if (len(stack) > 0 and stack[-1] == '('):
        stack.pop()
    else:
        return "No"

    while(len(stack) > 1):

        if (stack[-1] == '('):
            del stack[-2]
        else:
            del stack[-1]
    return "Yes"

if __name__=='__main__':
    lst = []
    for str in input().split():
        lst.append(str)
    print(match_parens(lst))


"""
TEST CASES...


print(match_parens(['()(', ')'])
print(

print(match_parens([')', ')'])

