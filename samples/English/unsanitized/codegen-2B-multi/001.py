from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    nested_paren_groups = paren_string.split('( )')
    for n in range(len(nested_paren_groups)):
        if any(word_group[n] == '()' for word_group in nested_paren_groups):
            nested_paren_groups[n] = '()'
            n += 1
            while any(nested_paren_groups[i] == '()' for i in range(n, len(nested_paren_groups))):
                nested_paren_groups[i] = ''
                n += 1
    return [nested_paren_groups[i] for i in range(0, len(nested_paren_groups)) if nested_paren_groups[i]!= '']


