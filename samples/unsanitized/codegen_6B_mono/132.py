
def is_nested(string):
    """
    Ek function banao jo sirf square brackets wala string input ke roop mein leta hai.
    Function tabhi True return karega jab valid subsequence of brackets ho 
    jisme kam se kam ek bracket nested ho.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    is_brac = lambda x: ['[',']']
    left = 0
    stack = []

    for right, item in enumerate(string,start = 0):
        if item in is_brac:
            if len(stack) == 0:
                return False
            if is_brac(item) == is_brac(stack[-1]) and len(stack)>1:
                stack.pop()
            else:
                stack.append(item)
    if len(stack) == 0:
        return True
    return False


#Alternate Solution

