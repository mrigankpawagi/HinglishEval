from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens_list = []
    for r in repr(paren_string):
        if len(r) <= 1:
            raise ValueError("Invalid parens")
        else:
            parens_list.append(r[0])

    return sorted(parens_list)

if __name__ == "__main__":
    parser = OptionParser(usage = """
Input:

python foo1.py foobar2
foo2

Output: foobar1(bar)(baz)(c++)(doit)

E.g
foo1 =...
foo2 =...
foo1.doit(bar, 'baz')

Output:

foo2

E.g.
>>> option.format() == '\\(foo\\)'
True
>>> option.format() == '\\((foo\\))('
True

E.g.
>>> option.format() == '\\(foo(()(()()))()')
False
>>> option.format() == '\\(foo(())(),(()()))()'
False

>>> option.format() == c("((foo((((...)))))()())))")
False

E.g.
>>> option.format() == c("((\\((((...))))))()))")
False

E.g.
>>> option.format() == c
False

DictLike
```Python

class DictLike(dict):
    """