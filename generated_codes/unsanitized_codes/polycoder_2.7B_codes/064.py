
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    vowels1, vowels2 = map(ch, s) if isinstance(s, str) else s
    n = len(s)
    return ((vowels1 == 'a' and 1 or vowels1 == 'e' and n % 2) and
            (vowels2 == 'a' and 4 or vowels2 == 'c' and 5))

