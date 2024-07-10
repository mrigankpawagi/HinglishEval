

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    # Write your code here.
    stack_lst = []
    for char in brackets:
        if char == '(':
            stack_lst.append(char)
        elif char == ')':
            if len(stack_lst) == 0:
                return False
            else:
                stack_lst.pop()
    return len(stack_lst) == 0
    
    # time: O(n), space: O(n)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

#####################################################

def double_bracket(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> double_bracket("(")
    True
    >>> double_bracket("()")
    True
    >>> double_bracket("(()())")
    True
    >>> double_bracket(")(()")
    False
    """
    # Write your code here.
    for bracket in brackets:
        if bracket == '(':
            brackets.remove(bracket)
    return len(brackets) < len(brackets[::-1])
    # time: O(n), space: O(1)
        
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

#####################################################
        
from string import ascii_uppercase
def solveB(name):
    """ The name of a person is given in a string. The name consists of exactly
    uppercase and lowercase Latin letters. Every uppercase letter has a corresponding
    lowercase letter, but there might be lowercase letters that don't have a corresponding
    uppercase letter. Write a function solveB(name). It should return an uppercase 
    version of the name, assuming all letters are of lower case.
    If the name is not correctly written, solveB(name) should return the input-
    string.

    >>> solveB("aBc")
    "ABC"
    >>> solveB("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    >>> solveB("")
    ""
    >>> solveB("abc")
    "ABC"
    >>> solveB("aBcX")
    "ABCX"
    >>> solveB("1