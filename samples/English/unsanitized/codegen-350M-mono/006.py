from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    
    # For each paren in the string
    prev = -1
    depth = 0  # To keep track of nesting depth
    paren_stack = list()
    for c in paren_string:
        if c == '(':
            depth += 1
            paren_stack.append(depth)
        elif c == ')':
            depth -= 1
            if depth:
                paren_stack[-1] += depth
            else:
                return depth
    # After the loop has exhausted the nested parentheses, the nesting depth
    return paren_stack \
        if depth == 0 else paren_stack[:-1]
    raise Exception('cannot parse nested parentheses {}'.format(paren_string))


