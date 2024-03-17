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
    opening_bracket_pos = brackets.lower().find("(")
    closing_bracket_pos = brackets.lower().find(")")
    return not opening_bracket_pos > closing_bracket_pos