from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    first_group = None
    while True:
        if first_group is None:
            first_group = []
        else:
            break
        for i, group:
            if first_group is not None:
                first_group.extend(Group([str(i) for __ in group]))
            first_group = group
            break
        else:
            break
    return first_group


