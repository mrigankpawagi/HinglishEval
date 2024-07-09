from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    paren_dict = {")": "(", "}": "{", "]": "["}
    for str in paren_string:
        if str == "(" or str == "{" or str == "[":
            paren_stack.append(str)
        elif str == ")" or str == "}" or str == "]":
            # if an } is encountered check if that is the last {}
            # if so add it to a list and break
            if len(paren_stack) == 0 or paren_dict[str]!= paren_stack[-1]:
                paren_stack.pop()
            else:
                paren_stack.pop()
                break

    # check if the list is empty
    if len(paren_stack) > 0:
        return [-1]
    return [len(paren_stack)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
