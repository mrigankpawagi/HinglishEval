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
    if len(string) % 2 == 1:
        return False

    stack = []
    for c in string:
        if c == "]":
            top = stack.pop()
            if top == "[":
                stack.append(top)
            else:
                return False

        elif c == "}":

            top = stack.pop()
            if top == "{":
                stack.append(top)
            else:
                return False

        elif c == ")":

            top = stack.pop()
            if top == "(":
                stack.append(top)
            else:
                return False

        elif c == "(":
            if stack:
                stack.append(c)
            else:
                return False

        stack.append(c)
    if stack:
        return False

    return True
