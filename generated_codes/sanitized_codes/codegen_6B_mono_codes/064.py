
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    d = {}
    for c in s.lower():
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1
    return d
