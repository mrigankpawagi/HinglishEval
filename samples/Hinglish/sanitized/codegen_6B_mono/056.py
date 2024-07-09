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
    stack = []
    closing_brackets = ("}", "]", ")", ">")
    if brackets == "":
        return True
    if brackets[0] not in closing_brackets:
        return False
    for bracket in brackets:
        if bracket in closing_brackets:
            if len(stack) == 0 or stack[-1] != bracket:
                return False
            stack.pop()
        else:
            stack.append(bracket)
    return True if len(stack) == 0 else False