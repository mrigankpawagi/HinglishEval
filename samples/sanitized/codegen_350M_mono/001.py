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
    new_arr: List[str] = []
    parsed = []
    for char in paren_string:
        if char == "(":
            parsed.append("(")
        elif char == ")":
            parsed.append(")")
        elif char == ")":
            char = parsed.pop()
            if char != "(":
                new_arr.append(char)
        else:
            new_arr.append(char)
            pass
    return new_arr