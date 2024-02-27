from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    stack = []
    groups = []
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            group = ""
            while stack[-1] != "(":
                group = stack.pop() + group
            stack.pop()  # remove the opening bracket
            group = "(" + group + ")"
            if stack and stack[-1] != "(":
                stack[-1] += group
            else:
                stack.append(group)
    return stack
