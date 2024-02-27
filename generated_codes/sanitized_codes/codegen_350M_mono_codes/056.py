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
    result = []
    for bracket in brackets:
        if bracket == "<":
            result.append("(")
        elif bracket == ">":
            result.append(")")
        elif bracket == "," or bracket == ".":
            result.append(bracket)
        else:
            result.append(bracket)
    if brackets not in result:
        return False
    else:
        return True