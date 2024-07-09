from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    group_keys: List[int] = []
    while paren_string:
        m = paren_string.find('(')
        if m > -1:
            group_key = group_keys[-1]
            group_keys.pop(-1)
            return group_keys, group_key, m
        token, group_key, m = paren_string.find('(', paren_string.find(",") + 1)
        if m > -1:
            group_key = group_keys[-1]
            group_keys.pop(-1)
            return group_keys, group_key, m
    return group_keys, 0, 0

