from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain nested parentheses ke. Aapka goal hai
    un groups ko alag alag strings me separate karna aur unki list return karni hai.
    Separate groups balanced hote hain (har open brace sahi se close hota hai) aur ek dusre ke andar nested nahi hote
    Input string me koi bhi spaces ko ignore karo.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    stack = []
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                groups.append("".join(stack[1:]))
                stack.pop()
            stack.pop()
    while stack:
        groups.append("".join(stack[1:]))
        stack.pop()
    return groups