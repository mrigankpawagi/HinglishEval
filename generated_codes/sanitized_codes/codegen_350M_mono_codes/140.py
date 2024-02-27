def fix_spaces(text):
    """
    Diye gaye string text mein, saare spaces ko underscores se replace karo,
    aur agar ek string mein 2 se zyada consecutive spaces ho,
    toh saare consecutive spaces ko - se replace karo.
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = []
    temp_list = list(text)
    for i in temp_list:
        if i == "":
            result.append("_")
        elif i == ".":
            result.append("-")
        elif i == "!" or i == "?" or i == ":":
            result.append("_")
        else:
            result.append(i)
    return "".join(result)