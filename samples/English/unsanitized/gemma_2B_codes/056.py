

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
    
    # This is a good start, but I want to move the code up one row.
    # Also, I want to include an error, and handle it appropriately.
    # You'll need to make the rest of the function.
    
    for i in range(len(brackets)-1):
        if brackets[i] == "<" and brackets[i+1] == ">":
            brackets += "<>"
        elif brackets[i] == "<" and brackets[i+1] != ">":
            brackets += ">>"
        elif brackets[i] == ">" and brackets[i+1] != "<":
            brackets += "<>"
        elif brackets[i] != ">" and brackets[i+1] == "<":
            return False
        
    return True
    
if __name__ == "__main__":
    #import doctest; doctest.testmod()
    print(correct_bracketing("<"))
    print(correct_bracketing("<>"))
    print(correct_bracketing("<<><>>"))
    print(correct_bracketing("><<>"))
