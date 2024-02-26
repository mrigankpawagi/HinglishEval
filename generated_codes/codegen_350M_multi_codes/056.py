

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
    brackets = string.rstrip("<>")
    brackets = brackets.split("<")
    # remove any empty brackets
    delimiters = brackets[0]
    delimit = delimiters.find("<<")
    delimiteven = delimiters.find(">>")
    if len(delimiters) >= 1:  # remove closing bracket
        delimitete = delimiters[-1]
        delimit = delimititeven
    else:
        delimitete = ""
    return delimit_left(brackets, delimit, delimitete)

