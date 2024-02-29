

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
    # your code here
    if len(brackets) % 2 != 0:
        return False
    else:
        for i in range(len(brackets)):
            if brackets[i] == "<":
                if brackets[i + 1] == ">":
                    return True
                else:
                    return False
            elif brackets[i] == ">":
                if brackets[i - 1] == "<":
                    return True
                else:
                    return False
    return True


def correct_bracketing_2(brackets: str):
    """
    brackets ek string hai "<" aur ">" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing_2("<")
    False
    >>> correct_bracketing_2("<>")
    True
    >>> correct_bracketing_2("<<><>>")
    True
    >>> correct_bracketing_2("><<>")
    False
    """
    # your code here
    if len(brackets) % 2 != 0:
        return False
    else:
        for i in range(len(brackets)):
            if brackets[i] == "<":
                if brackets[i + 1] == ">":
                    return True
                else:
                    return False
            elif brackets[i] == ">":
                if brackets[i - 1] == "<":
                    return True
                else:
                    return False
    return True


def correct_bracketing_3(brackets: str):
    """
    brackets ek string hai "<" aur ">" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing_3("<")
    False
    >>> correct_bracketing_3("<>")
    True
    >>> correct_bracketing_3("<<><>>")
    True
    >>> correct_bracketing_3("><<>")
    False
    """
    # your code here
    if len(brackets) % 2 != 0:
        return False
    else:
        for i in range(len(brackets)):
            if brackets[i] == "<":
                if brackets[i + 1] ==