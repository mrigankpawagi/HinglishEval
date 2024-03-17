

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
    """   brick_opened = False
    count = 0

    for character in brackets:
        if character == "[":
            count += 1
        elif character == "]":
            count -= 1
            if count < 0:
                raise ValueError("bracketing is incorrect")

        if character == "<" and not brick_opened:
            brick_opened = True
        elif character == ">" and brick_opened is True:
            brick_opened = False

    return bricks_open_bracket_closed

