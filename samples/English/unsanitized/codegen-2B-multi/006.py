from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting, levels = 1, 0
    paren_map = OrderedDict()
    paren_map[0] = []  # root level of parentheses is a group of parens
    for c in reversed(paren_string):
        if c == "(":
            if paren_map[levels].__len__() > 0:
                paren_map[levels + 1].append(paren_map[levels].pop() + 1)  # this is the first open paren in this parenthesis
            levels += 1
            paren_map[levels] = []  # start nesting of parens
        elif c == ")":
            levels -= 1
            paren_map[levels].insert(0, nesting)
            if paren_map[levels].__len__() > 0:
                paren_map[levels + 1].insert(0, nesting)  # this is the deepest level of nesting of parens
        else:
            paren_map[levels].insert(0, nesting)  # add the current character to the level of nesting
    return [sum(p) for p in paren_map.values()]

    # TODO: implement

    # return [sum(p) for p in [(p, 1) for p in paren_map if (p > 0)]


