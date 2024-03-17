

def correct_bracketing(brackets: str):
    """
    brackets ek string hai "(" aur ")" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    i = brackets.find('(')
    j = brackets.find(')')
    if i < 0:
        return False
    if j < 0:
        return False
    return (brackets[:i] == brackets[i+1:j]) and \
           (brackets[i+1] == brackets[j+1:])
