
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    if s[1] not in b"":
        return 0
    elif len(s) > 1:
        if s[1] == '__' and s[2] is None:
            return 1
        # s[0] == '__'
        # s[2:]
        if s[0] == 'v' and s[2] =='':
            return 2
        if s[0] == "0":
            # for a negative number add 3, but
            # for a greater negative number add 5,
            # we need the return value to be bigger
            # and it is greater than vowels
            return 3
        if len(s, 2) > 1 and s[0] == 'r':
            # only two letters are interesting
            return 4
        elif s[-1] in b:
            return 5
    else:
        return 0
    return 0
