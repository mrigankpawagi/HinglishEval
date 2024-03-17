from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = []
    max_level = 0
    current_level = 0
    for char in paren_string:
        if char == "(":
            current_level += 1
            max_level = max(max_level, current_level)
        elif char == ")":
            current_level -= 1
    for char in paren_string:
        if char == "(":
            current_level += 1
            if current_level == max_level:
                levels.append(max_level)
        elif char == ")":
            current_level -= 1
    return levels
