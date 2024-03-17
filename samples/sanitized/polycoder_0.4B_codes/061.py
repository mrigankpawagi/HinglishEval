

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
    bracket_list = brackets.split(")")
    bracket_list.sort(key=lambda x: x.replace("-", ""), inplace=True)
    bracket_list.pop(0)
    bracket_list.reverse()
    bracked_list = bracket_list[:]
    bracked_list.sort(key=lambda x: x.replace("(", ""), inplace=True)
    bracked_list.reversed()

    bracket_left = "("
    bracket_right = ")"
    # first-bracket is on first-level bracket
    bracket_number = bracket_left.count("(") - 1
    bracket_number += bracket_list.count("(")
    bracket_number += bracket_right.count(")"))
    if bracket_number!= 1:
        return False

    bracket = bracket_list[0]
    for level in bracket_list[1:]:
        bracket_number = bracket["("].count("(") - 1
        bracket_number += bracket_list.count("(")
        bracket_number += bracket_right.count(")")
        level = level.replace(")", ";")
        level = level.replace("]", ", ")
        bracked_list += (
            "(" + bracket["("] + bracket_right + "{"), level)
        ).replace(")",