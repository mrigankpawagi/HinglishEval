from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nlevel = len(paren_string) // 2
    parens = []
    while nlevel:
        a, _level = nlevel // 2, nlevel % nlevel
        paren_start = paren_string[:a]
        a -= a % 2
        if a:
            paren_string = paren_string[a:]
        parens.append(paren_start)
        nlevel -= 1
    return parens


class Parser:
    def __init__(self) -> None:
        self.state = ['expr']

    def parse(self) -> List[str]:
        return list(self._parse())

    def peek(self) -> Optional[str]:
        if len(self._parse()) == 0:
            return None

        if isinstance(self._parse()[0], (tuple, list, iter, tuple, list)):
            # if inside list, remove leading '(', if present
            # then it's a list
            item_list = self._parse()[0]

         