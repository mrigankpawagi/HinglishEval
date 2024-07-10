
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

    is_subsequence = True
    for i, l  in enumerate(string):

        if(l == '['):
            if(i + 1 == len(string)):
                return False
            elif(string[i + 1] != ']'):
                return False
            else:
                continue

        if(l != '['):
            return False
    return is_subsequence
