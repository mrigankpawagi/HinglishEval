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
    paren_group_list = []
    string_list = paren_string.split('"')
    prev_string = ""

    def separate_paren_group(current_string: str) -> List[str]:
        """
        Is function ka input ek string hota hai jisme multiple groups hote hain nested parentheses ke. Aapka
        goal hai un groups ko alag alag strings me separate karna aur unki list return karni hai. Separate
        groups balanced hote hain (har open brace sahi se close hota hai) aur ek dusre ke andar nested nahi hote
        Input string me koi bhi spaces ko ignore karo.
        >>> separate_paren_group('()()(()')
        ['()', '(())']
        """
        global previous_string
        if len(current_string) == 0:
            pass  # Ignore empty input string.
        elif previous_string not in string_list:
      