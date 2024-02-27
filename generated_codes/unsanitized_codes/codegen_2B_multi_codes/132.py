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

    if string:
        level, index = 0, 0
        for x in string:
            if x == "[":
                level += 1
            elif x == "]":
                level -= 1
            elif x == "[" and level == 1:
                index += 1
            elif x == "]" and level == -1:
                index -= 1
        return index > 1

    else:
        return False
