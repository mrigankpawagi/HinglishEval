from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # result = []
    level = 0
    parenthesis = 0
    opening = ["(", "[", "<"]
    for c in paren_string:
        if c in opening and parenthesis == 0:
            level += 1
            parenthesis += 1
        elif ")".encode() in c.encode():
            parenthesis -= 1
    return level