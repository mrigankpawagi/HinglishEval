
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
    is_square_bracket = lambda string: '[' not in string  and  '[' in string and ']' not in string
    
    if is_square_bracket(string):
        return True
    else:
        return False

print(is_nested('[[]]')) #True
print(is_nested('[[[]]]')) #True
print(is_nested('[[[[]]][[]][[]]][[[[]]]')) #True
print(is_nested('[[[[[[]]][[]][[]]][[[[[[]]]]][[[[]]]')) #True
