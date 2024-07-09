

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    closed_brackets = ""
    open_brackets = brackets
    for b in open_brackets:
        # check for the existence of the corresponding closed bracket
        for c in closed_brackets:
            if (b == c) and (not closed_brackets.startswith(c)):
                return False
        # check for the presence of an unpaired left- or right-parenthesis
        if (b == "(") and (b!= ")":
            return False
        if (b == ")" and (b!= "("):
            return False
        close_brackets += b and open_brackets[len(open_brackets)-1:len(open_brackets)-1]
    return not closed_brackets


# vim: tabstop=8 expandtab shiftwidth=8 ft=python
