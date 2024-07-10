from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if paren_string in ['()', '(', ')']:
        return [len(paren_string) - 1]
    if paren_string[0] == '(':
        res, sub_res = parse_nested_parens(paren_string[1:]), parse_nested_parens(paren_string[2:])
        return [1, res[-1]]
    else:
        res = []
        while paren_string:
            if paren_string[0] != '(':
                res.append(len(paren_string))
                paren_string = paren_string[1:]
            else:
                new_parens = paren_string[paren_string.index('('):]
                res.append(len(max(parse_nested_parens(new_parens), key=len)))
                paren_string = paren_string[len(new_parens):]
        return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
