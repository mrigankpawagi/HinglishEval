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
    if "_()" not in brackets:
        return False
    opening_parenthesis = brackets.find("(").parent.parent
    closing_parenthesis = brackets.find(")").parent.parent
    if opening_parenthesis > -1:
        closing_parenthesis = brackets[
            opening_parenthesis + 1 : opening_parenthesis + 1
        ]
        if closing_parenthesis > -1 and closing_parenthesis[-1] == "(":
            return True
        return False
    else:
        return False