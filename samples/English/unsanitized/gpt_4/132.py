def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack or stack.pop() != '[':
                return False
    return len(stack) == 0 and '][' not in string