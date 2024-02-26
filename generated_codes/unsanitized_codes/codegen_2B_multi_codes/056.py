

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
    opening_brackets = []
    closing_brackets = []
    for brackets in brackets.split(""):
        if brackets[-1:] == ">":
            closing_brackets.append(brackets[:-1])
        elif brackets[-1:] == "<":
            opening_brackets.append(brackets[:-1])
        elif brackets[:-1] == "<<><>>":
            closing_brackets.extend([brackets[:-1] + ">" + x for x in opening_brackets])
        elif brackets[:-1] == ">" + "<<>":
            closing_brackets.extend([brackets[:-1], brackets[-1:] + ">" + opening_brackets[-1]])
    return closing_brackets == opening_brackets
