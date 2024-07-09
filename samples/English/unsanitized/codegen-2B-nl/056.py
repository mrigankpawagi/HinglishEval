

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    if not brackets:
        return False

    first_bracket = brackets.find('<')
    last_bracket = brackets.find('>')

    if first_bracket or last_bracket:
        return False
    elif first_bracket < last_bracket:
        return False

    return True


##########################################################################
# Generates the first level of the dependency graph.
##########################################################################
