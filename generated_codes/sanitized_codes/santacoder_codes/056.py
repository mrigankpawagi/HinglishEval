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

    i = 0
    while i < len(brackets):
        if brackets[i] == "<":
            if brackets[i - 1] == "<":
                brackets = replace_in(brackets, i, i)
                i += 1
            else:
                brackets = replace_in(brackets, i, i - 1)
                i += 1
        else:
            # hara < ka ek <
            i += 1
    return True
