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
    left_count = 0
    right_count = 0
    # 1. initial conditions
    for i in range(0, len(brackets)):
        if brackets[i] == "<":
            left_count += 1
        if brackets[i] == ">":
            right_count += 1
    #    print(left_count, right_count)
    #    print(correct_bracketing("> < \t") == False)
    return left_count == right_count