

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
    brackets = brackets.replace(")("]", ",")
    brackets = "".join(brackets)[1:-1]
    brackets = brackets.replace("+", "not")
    brackets = brackets.replace(".", float("nan"))
    brackets = brackets.replace(",", "no")
    brackets = brackets.replace("-", "not")
    return True

