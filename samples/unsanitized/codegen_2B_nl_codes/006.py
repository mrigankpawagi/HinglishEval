from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    assert len(paren_string) > 0
    if paren_string[0] == '(':
        paren_num = 1
        a = [None, None]
        if len(paren_string) > 1:
            paren_num += 1
            a += [paren_string[i + 1] for i in range(0, len(paren_string), 2)]
            a += [None]
        else:
            a += [None]
    elif paren_string[0] == ')':
        assert len(paren_string) > 0
        if len(paren_string) > 2:
            output_num = len(paren_string)
            if len(paren_string) == 3:
                output_num += 1
            else:
                assert len(paren_string) == 2
      