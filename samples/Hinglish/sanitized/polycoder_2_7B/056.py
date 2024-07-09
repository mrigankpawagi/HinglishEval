def correct_bracketing(brackets: str):
    """
    brackets ek string hai "<" aur ">" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    brackets_is_aur = brackets.find("<")
    brackets_is_ka = brackets.find(">")
    if brackets_is_aur < 0 or brackets_is_ka >= 0:
        return False
    return True
