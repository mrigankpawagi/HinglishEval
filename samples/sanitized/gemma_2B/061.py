

def correct_bracketing(brackets: str):
    """
    brackets ek string hai "(" aur ")" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # your code here
    if len(brackets) % 2 == 1:
        return False
    else:
        stack = []
        for bracket in brackets:
            if bracket == "(":
                stack.append(")")
            elif bracket == ")":
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

