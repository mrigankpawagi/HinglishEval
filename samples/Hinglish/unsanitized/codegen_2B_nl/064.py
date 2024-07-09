
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    a,e,o,u = 'aeou', 'aeoou', 'aoou', 'aoa', 0, 0, 0, 0, 0
    b,i,n = 'biin', 'biin', 'bin', 'bin', 0, 0, 0, 0

    for c in s:
        if c[:2] in 'aeo':
            a += 1
        else:
            b += 1
            if c[1:3] == 'in':
                e += 1
            if c[3:4] == 'ou':
                o += 1
                if c[3:5] == 'ou':
                    o += 1
            if c == 'ai':
                u += 1

    return (a, b, e, o, u)

