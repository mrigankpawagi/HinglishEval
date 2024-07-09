
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
    if len(string) >= 1 and string[0] in '(){[][[]':
        first_char_is_nested = '[[' in string
        second_nested = False
        if is_nested(string[:-2]):
            second_nested =<mask_1>_nested:
                second_nested = True
        else:
            second_nested = False
        return first_char_is_nested and second_nested
    return False