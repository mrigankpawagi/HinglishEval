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
    def count_opening(group_count: int):
        """
        Count opening parenthesis
        :param group_count: count number of open parenthesis in given string
        :return: Opening parenthesis count
        """
        count = 0
        for char in group_count:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def count_closing(group_count: int):
        """
        Count closing parenthesis
        :param group_count: count number of closed parenthesis in given string
        :return: Closing parenthesis count
        """
        count = 0
        for char in group_count:
            if char == ')':
     