

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
    if len(brackets)!= len(str(brackets)+1):
        return False

    for i, c in enumerate(brackets):
        if c!="/":
            if c!= "<" and not isalpha(c) or ">" == c:
                raise ValueError("No opening or closing bracket found")

    return True
