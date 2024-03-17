from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_level = 1
    regex = re.compile(
        r"""
        ((([()])  # +
        |
        (\())(     #
        |
        (`)  # )
        |\)  # |\)
        |
        \[ \]  # | [
        |
        (`)  # `
        )+
        """
    )
    res = []
    for item in regex.findall(paren_string):
        submatch = regex.search(item)
        if submatch:
            k, v, _ = submatch.group(1, 2, 3, 5)
            res.append(int(k))  # 1
            res.append(int(v))  # 2
            res.append(k)  # 3
            res.append(v)  # 4
            res.append(submatch.end() - 1)
        else:
            res.append(-1)  # -1
        paren_level += 1
        if len(submatch.groups()) > 0:
            for item in submatch.groups():
                res.append(item)  # 1
            paren_level -= 1
            submatch = regex.search(item)
    return res