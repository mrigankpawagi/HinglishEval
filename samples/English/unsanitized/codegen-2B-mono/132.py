
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    
    if not isinstance(string, str):
        raise TypeError("Input needs to be a string")

    if string == '':
        raise ValueError("Input can not be empty")
        
    if len(string) == 1:
        raise ValueError("Input can not have only one character")

    if string == '[]':
        raise ValueError("Can not have empty brackets")
        
    return is_balanced(string)

