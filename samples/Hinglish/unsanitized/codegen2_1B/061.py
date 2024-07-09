

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
    for bracket, char_to_match in brackets.split("{"):
        if "(" in bracket and ")" in bracket:
            counts_correct_bracket = 0
            is_open_bracket_found = False
            counts = bracket.count(char_to_match)
            if counts["("] == 4 or "+" in ["1", "+"].intersection(["1", "+"]*counts["("]+counts[")"]):
                is_open_bracket_found = True
            if counts["("] * 3 == counts["+"] * 3 and counts["("] + counts["+"] * 3 == counts["+"] + counts.count("+")) or is_open_bracket_found:
                counts_correct_bracket += counts["+"]["*3]
                counts_correct_bracket -= counts["("] * 3
            if counts["("] * 3 >= counts.count(char_to_match) * 2 and not(is_open_bracket_found):
                counts_correct_bracket = counts_correct_bracket + counts[")"]["*3]
        if is_open_bracket_found:
            return counts_correct_bracket
    return None


