from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # base case of recursion
    if len(paren_string) == 0:
        return []

    # split list when bracket is found
    bracket_indices = [i for i, x in enumerate(paren_string) if x == '(']
    open_bracket, *inner_bracket_remainers = bracket_indices

    # recurse based on first sub-list
    first_element_list = separate_paren_groups(paren_string[:open_bracket])

    for index2 in range(len(first_element_list)):
        first_element_list[index2] += paren_string[opening_bracket + 1:inner_bracket_remainers[0]]

    inner_brace_remainers = inner_bracket_remainers[1:]
    # if there are any remaining inner brackets, make separate list
    if len(inner_brace_remainers) > 0:
        second_element_list = separate_paren_groups(paren_string[open_bracket + 1:inner_brace_remainers[0]])
        first_element_list += second_element_list
    else:
        first_element_list.append(paren_string[open_bracket+1:inner_brace_remainers[0]])  # first element list

    return first_element_list


