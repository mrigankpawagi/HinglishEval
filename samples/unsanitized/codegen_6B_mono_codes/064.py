
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

if __name__ == '__main__':
    assert vowels_count('Python') == {'p':1, 'y':1, 't':1, 'h':1, 'n':1, 'o':1}
    assert vowels_count('Python - 1') == {'p':1, 'y':1, 't':1, 'h':1, 'n':1, 'o':1}
    assert vowels_count('1') == {}

    print FIX
