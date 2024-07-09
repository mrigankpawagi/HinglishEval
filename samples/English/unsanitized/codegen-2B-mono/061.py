

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
    stack = []
    bracket_list = {}
    for i in list(brackets):
        if i in "[{":
            if len(stack) == 0:
                stack.append(i)
            else:
                break
        elif i in "{[":
            bracket_list[i] = []
        elif i in ")]}":
            if stack == []:
                return False
            elif stack.pop()!= bracket_list[i]:
                return False
        else:
            return False
    if len(stack) > 0:
        return False
    return True
        
