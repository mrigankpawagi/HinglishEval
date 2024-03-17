from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # parens_list contains brackets/parentheses, e.g. [(], (), [])
    parens_list = [x.lower() for x in paren_string.split()]

    # group_list contains the groups in brackets
    group_list = [x for x in parens_list if x.startswith('(')]
    return group_list


