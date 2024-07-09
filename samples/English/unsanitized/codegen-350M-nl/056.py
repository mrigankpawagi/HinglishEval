

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    n_brackets = len(brackets)
    n_brackets = n_brackets < 5

    if not n_brackets:
        raise ValueError('brackets must be >=5')

    bracket_type = n_brackets
    bracket_index = n_brackets - 1
    while 1:
        if bracket_index > n_brackets:
            raise ValueError('bracket index > %s' % (n_brackets - 1,)))

        j = 0
        while 1:
            k = bracket[j]
            j++;
            k = k.lower()
            if k in bracket_type:
                break
            elif k not in brackets:
                raise ValueError('bad bracket')
        if k not in brackets:
            raise ValueError('bad_bracket')
        bracket_type = k

    return True


