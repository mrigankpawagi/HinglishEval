from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stak = []

    for ch in paren_string:
        if ch == "(":
            stak.append(ch)
        if ch == ")":
            if len(stak) > 0 and stak[-1] == "(":
                stak.pop()
                max_level = len(stak)
            else:
                return ValueError("Unbalanced parenthesis")

    return [max_level] if stak == [] else ValueError("Unbalanced parenthesis")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
