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
    if not paren_string:
        return []

    parens = []
    string = []

    for char in paren_string:
        if char == '(':
            parens.append(char)
            string.append(char)
        elif char == ')':
            group = "".join(string)
            parens.append(group)
            string.clear()
        else:
            if len(string)!= 0:
                group = "".join(string)
                parens.append(group)
                string.clear()
            parens.append(char)

    return [str(paren) for paren in parens if paren!= '']

