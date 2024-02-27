

def correct_bracketing(brackets: str):
    """
    brackets ek string hai "(" aur ")" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    def helper_function(opening_bracket, closing_bracket):
        bracket_dict = {}
        for bracket in opening_bracket:
            if bracket not in bracket_dict:
                bracket_dict[bracket] = 0

            bracket_dict[bracket] += 1

        if bracket_dict[closing_bracket] <= 0:
            return False

        bracket_dict[closing_bracket] -= 1
        return True

    # return helper_function(brackets, brackets[0]) and helper_function(brackets, brackets[-1])
    return helper_function(brackets, brackets[1]) or helper_function(brackets, brackets[-2])


