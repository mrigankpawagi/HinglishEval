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
    brackets_key_list = []
    for bracket in brackets:
        if bracket == "<>":
            brackets_key_list.append(">")
        else:
            brackets_key_list.append(bracket.lower())
        bracket_key = brackets_key_list[bracket_key_index]
        bracket_key_index += 1
        if bracket_key_index == len(brackets_key_list) - 1:
            return True
    return False
