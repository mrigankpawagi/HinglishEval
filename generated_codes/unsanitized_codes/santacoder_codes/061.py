

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
    openi_dict = {")": "(", "}": "{", "]": "["}
    openl_dict = { ")": "(", "}": "{", "]": "["}

    if len(brackets) < 1:
        return False

    stack = []
    for bracket in brackets:
        if bracket in openl_dict:
            stack.append(openl_dict[bracket])
            continue
        if bracket in openi_dict:
            if not stack or stack.pop()!= openi_dict[bracket]:
                return False
    return True

