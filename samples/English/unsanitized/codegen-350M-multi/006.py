from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    out_list = []
    for index, char in enumerate(paren_string):
        if char == '(':
            new_index = index
            while new_index < len(paren_string) and paren_string[new_index].isdigit():
                new_index += 1
            out_list.append(int(new_index))
            continue
        elif char == ')':
            if out_list[-1] == 0:
                out_list[-1] = new_index + 2
            elif out_list[-1] == 1:
                out_list.append(index)
                out_list[-1] += 1
            else:
                raise RuntimeError('Unable to unify parentheses for {}'.format(index))
            continue
        elif 0 <= char.lower() <= 'z':
            out_list.append(int(index))
            continue
        elif ')()' in paren_string:
            raise RuntimeError('Unable to unify parentheses for {}'.format(index))
        elif '()' in paren_string:
            raise RuntimeError('Unable to unify parentheses for {}'.format(index))
        elif '(' in paren_string:
            paren_counter = 0
            for char in paren_string[index:index + (index + 1)]:
                out_list.append(index)
                out_list.append(int(char))
                if char == '(':
                    paren_counter += 1
                else:
                    if char == ')':
                        if paren_counter == 1 or paren_counter is None:
                            raise RuntimeError('Unable