

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
    n_opening = 0
    for i, x in enumerate(brackets):
        # check opening bracket of length > 2
        if len(x) > 2):
            opening = brackets[i - n_opening]
            if opening == ")":  # (end of string)
                if i >= len(brackets)-1:
                    return False
            elif i < len(brackets)-1 and brackets[i + 1] == ")":  # (beginning), do nothing
                pass
            elif not(open_bracket(x) == closing): return False  # opening bracket not correct
        n_opening += 1
    return True


