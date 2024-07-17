
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
    if string.replace('[', '').replace(']', '').replace('[[', '').replace(']', '').replace('[[', '').replace(']]', '').replace('[''', '').replace('[]', '').replace(']]', '').replace('[', '').replace(']', '').replace(']', '').replace(']', '') == '':
        return False
    else:
        return True
