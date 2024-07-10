from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if paren_string:
        return_list = []
        cur_paren = ""
        for char in paren_string:
            if char != " ":  # Don't add space in return list to avoid it as part of a paren
                try:
                    if cur_string == "(":
                        cur_paren = cur_paren + char
                    elif cur_string == ")":
                        return_list.append(cur_paren)
                        cur_paren = ""
                except:
                    print("No match in string. ")

        elif cur_string == "(":  # Handle case if no nested parenthesis string
            return_list.append(cur_paren)
            cur_paren = ""

    else:  # Handle case if entire string is just spaces
        return [""]

    return return_list
    # return_list = tuple([tuple(i.split()) for i in return_list])
    # return_list[1] = reverse_list
    # return return_list


print((separate_paren_groups("( ) (( )) (( )( ))")))
print((separate_paren_groups(" ") + " () () (") + " () ())"))
print((separate_paren_groups("  () () (  ( ) )\n    (   )   "))
