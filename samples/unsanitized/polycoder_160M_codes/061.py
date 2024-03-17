

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
    try:
        havocabs_string = re.sub(r"(\-|\\)" + brackets + r"\[\s()<>+@\-|\-\.\[+@,]+,?:" + r"\]", "", brackets)
        return bool(havocabs_string)
    except (UnicodeError, IndexError):
        return False
