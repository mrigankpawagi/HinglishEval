from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    group = parse_nested_parens.group(0)
    try:
        if group == int(k) and isinstance(k, int):
            return group + 1
        else:
            group = parse_nested_parens.group(parse_nested_parens.group_count(k))
    except ValueError:
        pass
    else:
        raise ValueError(
            "Please provide both a non-number and number, number format string, plus one additional separator and you will have to use a space after "
            "the end of that input"
        )