from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain jo nested parentheses se alag kiye gaye hote hain spaces ke dwara.
    Har group ke liye, sabse gehri level ki nesting of parentheses ka output do.
    Jaise ki, (()()) ka maximum do levels ki nesting hoti hai jabki ((())) ki teen hoti hai.
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    list_of_nesting = []
    counter = 0
    for index in range(len(paren_string)):
        if paren_string[index] == "(":
            counter += 1
            if paren_string[index + 1] == "(":
                counter += 1
                list_of_nesting.append({} for i in range(counter))
        parsed_out = []
        level = 0
        while level > 0:
            if level in [0, 1]:
                if index == len(paren_string) - 1:
                    break
                if paren_string[index + 1] == ")":
                    level -= 1
                    if len(paren_string) < index + 1:
                        list_of_nesting[counter - 1][level] = parsed_out
                    else:
                        previou_nested_index = parse_nested_parens(
                            paren_string[index + 2 :]
                        )
                        list_of_nesting[counter - 1][level].extend(previou_nested_index)
                    parsed_out = []
                    index += 2
                    continue
                else:
                    parsed_out.append(paren_string[index + 1])
                    index += 1
            elif paren_string[index] == ")":
                level -= 1
            elif paren_string[index] == "(":
                level += 1
            else:
                continue
        if parsed_out != []:
            list_of_