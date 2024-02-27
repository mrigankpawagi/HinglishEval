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
    paren_string = paren_string.replace(" ", "")
    paren_string_list = []
    stack = []
    for char in paren_string:
        if char == "(":
            if not len(stack) == 0:
                paren_string_list.append(stack)
            stack.append(char)
        elif char == ")" and len(stack) > 0:
            char = stack.pop()
        elif char != "":
            paren_string_list.append(char)
        elif char != "":
            continue
        else:
            paren_string_list.append(" ")
    return paren(paren_string_list)