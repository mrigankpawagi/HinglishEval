

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
    if len(brackets) > 1:
        return False

    k = brackets.index("<")
    if k > 0 and brackets[0] in (">", "--"):
        if isinstance(brackets[0], str):
            if len(brackets) > 1:
                return False
            elif len(brackets) > 1 and "-".join(brackets[0]) in ("<>"):
                return True
            else:
                return False
        return None

    return k

