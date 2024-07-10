from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # if string is empty return []
    lparen_index_list = []
    paren_string = paren_string.split(' ')
    for paren in paren_string:
        lparen_match = re.search('(..)*', paren)
        if lparen_match:
            lparen_index_list.append(int(lparen_match.group().count('(')))
        else:
            lparen_index_list.append(1)
    return [idx for idx in lparen_index_list if idx != 1]
