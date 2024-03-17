from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_index = -1
    paren_string_stack = []
    braces_level = 0
    paren_level = 0
    has_group = False
    paren_string_length = len(paren_string)
    while '(' in paren_string or ')' in paren_string:
        curr_char = paren_string[paren_index]
        if paren_char == ')':
            paren_level = paren_level - 1
            braces_level = braces_level - 1
            if braces_level <= 0:
                paren_string_stack.append(curr_char)
        elif paren_char == '{':
            braces_level = braces_level + 1
            paren_level = paren_level + 1
            if not braces_level == 0:
                paren_string = curr_char
            paren_string_stack.append(curr_char)
        elif paren_char == '}':
            paren_level = paren_level - 1
            braces_level = braces_level - 1
            if braces_level <= 0 and not paren_string_stack[-1] in {'(', '{'}:
                paren_string_stack.pop(-1)
            else:
                if paren_string_stack[-1] == '(' and paren_string_stack[-1] == '{':
                    paren_string_stack.pop(-1)
                    paren_string_stack.pop(-