from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output = []  # type: List[str]
    stack = []  # type: List[List[str]]

    in_paren = False
    in_bracket = False

    for x in paren_string:
        if (not in_paren and x == '(') and (not stack or not ((len(stack) > 1 and len(stack) == stack[-1] + 1) or (len(stack) == 0))):
            stack.append([])
        elif in_paren and x == '(':
            stack[-1].append(x)
        elif in_paren and x == ')':
            in_paren = False
            assert len(stack) >= 1
            if len(stack) == 1:
                output.append(paren_string[paren_string.index(stack[0][0])+1:paren_string.index(stack[0][-1])])
            else:
                cur_left = stack.pop()
                cur_right = stack[-1]
                if len(cur_right)!= 0:
                    assert (str(cur_right[0]) == str(cur_right[len(cur_right)-1])) or str(cur_right) in ['()', '[]'], \
                        'Nested brackets must close with matching opening brackets at {}'.format(str(cur_right))
                    cur_right = cur_right[0:-1]
                if (in_bracket and (len(cur_left)!= 0 or len(cur_right)!= 0)):
                    output.append('''({} {})'''.format(''.join(cur_left), ''.join(