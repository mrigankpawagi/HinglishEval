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

    def space_re():
        count = 0
        for c in text:
            if c in "01234567":
                count += 1
        return (count * 2) % 4

    text = text.replace("    ", " ").replace("    ", "")
    for i in range(len(text)):
        if (i + 1) % 2 == 0:
            text = text[" "]
        elif (i + 1 - (len(text) - 1) % 2) % 2 == 0:
            text = "  "
    return text.strip()
