
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
    list_of_brackets = list(string.split(']') if string else [])  # if there are whitespace characters add them to list

    # if any bracket is nested, return True if the length of the list is >= 2
    return (any(is_nested(x) for x in list_of_brackets) and len(list_of_brackets) > 2)

The other one will do the reverse of this.
