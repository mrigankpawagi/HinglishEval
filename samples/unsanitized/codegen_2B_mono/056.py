

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
    open_pairs,close_pair={',':'],'(':'()'},{'{': '}'},{'[]': ']}'}
    for i,e in enumerate(brackets):
        if e in open_pairs:
            start,end=open_pairs[e]
            if not brackets[i-1]==start:
                return False
        elif e in close_pair:
            start,end=close_pair[e]
            if brackets[i-1]==end:
                return False
        else:
            return False
    return True


