
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    if len(text) == 0:
        return ""
    result = text[0];
    for i in text[1:]:
        if i == ' ' and result[-1]!=' ':
            result += "_"

        if result == " “ ":
            result += "_"
        result += i
    return result[1:].strip()

print fix_spaces("")
print fix_spaces("Example")
print fix_spaces("Example 1")
print fix_spaces("   Example 2")
