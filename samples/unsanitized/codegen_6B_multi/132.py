
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
    if len(string) and string[0] == '[':
        return is_nested(string[1:])
    if len(string) and string[-1] == ']':
        return is_nested(string[-2:-1])
    if not len(string) or not string[0] or not string[-1]:
        return False

    # Check for [][][]...[] or [][] or [[] or [].
    if len(list(reversed(string))) % 2 == 0:
        if len(string) < 3 and string[0]!= '[':
            return False
        else:
            return True

    if not len(list(reversed(string) if len(list(reversed(string))) > 1 else string)) % 2 == 0:
        return False

    # Check if there is any unenclosed '[[['.
    return list(reversed(string))[0:][-3:-2] == ['[[[',] or \
        list(reversed(string) if len(list(reversed(string))) > 1 else string)[-3:-2] == ['[',] or \
        list(reversed(string) if len(list(reversed(string))) > 1 else string)!= ['[',]

