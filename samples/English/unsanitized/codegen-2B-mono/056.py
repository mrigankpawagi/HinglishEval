

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
    """
    If the 'brackets' list is empty, the stack is empty, so return True. 
    Otherwise you take the first (and only) bracket, push it on the stack. Once you have that bracket, 
    check the opposite bracket. If there's no bracket after the first one and you also have an index that refers 
    to where the last closing bracket was, then that index's value is 0, so check that before adding the closing bracket. 
    If there is not the same index in brackets as the stack has items(which may have value), we know we must pop from the stack. So 
    the return must be False. Because the returned value refers to the last closing bracket in Brackets; 
    this implies its matching opening bracket that should be in Bracketing. If it was not the case, then we must pop the stack.
    """
    if not brackets:
        return True 

    current_bracket = brackets[0]# first bracket in brackets
    brackets.pop(0)

    # add current_bracket to Brackets, and it's index to Bracketing
    Brackets += current_bracket
    Bracketing.append(current_bracket)

    while Bracketing and Bracketing[-1] == current_bracket:
        Bracketing.pop(-1)

    return Brackets in Bracketing  
