
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
    try:
        i = 0
        
        for char in string:
            if char == ']' and i > 0:
                return False
            if ((char == '[') or (char == ']')) and i < len(string):
                return False
            i += 1

        return True
    except Exception as e:
        e.args = (string, "Is_nested")
        raise e
    
print(is_nested('[][''))

# - - - - - - - - - - - - - - - - - - - #
'''
The string is a string where the brackets are nested
'''
