
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
    s = '['
    l = []
    for i in range(len(string)):
        if string[i] == '[':
            l.append(string[i])
        elif string[i] in s:
            l.append(string[i])
        elif len(l) == 0:
            if string[i] == ']':
                return False
    return len(l) == 0

print(is_nested('[[]]'))
print(is_nested('[[]]][[[[]]]'''))
print(is_nested('[][]][]'''))
print(is_nested('[]]]'))