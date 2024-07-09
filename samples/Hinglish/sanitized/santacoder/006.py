from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_groups = []
    counter = 0
    paren_string = paren_string.strip()
    paren_string = paren_string.replace(" ", "")
    # print(paren_string)
    for paren in paren_string:
        if paren == "(":
            counter += 1
        elif paren == ")":
            counter -= 1
        elif counter == 0:
            paren_groups.append(counter)

    return paren_groups
