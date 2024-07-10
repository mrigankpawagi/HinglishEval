

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
    "*** YOUR CODE HERE ***"
    stack = []
    for opening in brackets:
        if opening == "(":
            stack.append(opening)
        elif stack.pop() != "(":
            return False
    return True
    # return brackets.count('(') + brackets.count(')') == len(brackets) 

def balanced_brackets(code: str):
    """
    code ek string hai jise jo bhi syntax pehle se ho gayi ho woh remove kar diya hai.
    return ek function jo ek opening bracket aur ek corresponding closing bracket find kar de.
    opening bracket '(', ')', '{', '}', '[', ']'
    closing bracket '}', ']', ')'.

    """
    "*** YOUR CODE HERE ***"
    stack = []
    for bracket in code:
        if bracket not in "()[]{}":
            continue
        elif bracket in "([{":
            stack.append(bracket)
        elif not stack:
            return 
        elif bracket not in ")}]":
            stack.pop()
        else:
            return 
    if stack:
        return 
    return
