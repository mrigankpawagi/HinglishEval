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
    nesting_brackets = ["[", "{", "("]
    closing_brackets = ["]", "}", ")"]
    n = 0
    # print(list(string))
    for i in range(len(list(string))):
        # print(list(string)[i])
        if list(string)[i] in nesting_brackets:
            n += 1
            if n == 0:
                return True
            else:
                return False
        else:
            n = 0