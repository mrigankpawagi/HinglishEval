

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
    brackets = list(set(brackets))
    joint_brackets = []
    for i in range(0, len(brackets), 2):
        bracket1 = brackets[i]
        bracket2 = brackets[i+1]
        if "#" not in bracket1:
            if bracket1 == ">": # hai opening bracket ho gab gak ek
                joint_brackets.append(bracket2)
            else:
                joint_brackets.append(bracket1)


    bracket_found = False
    for i in joint_brackets:
        if len(i) == 3 and "#" in i:
            bracket_found = True # agar ka ekat ek
            break

    return bracket_found == False


    return correct_bracketing(joint_brackets)


