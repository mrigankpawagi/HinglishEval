from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    max_depths = []
    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == "(":
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ")":
                current_depth -= 1
        max_depths.append(max_depth)
    return max_depths
