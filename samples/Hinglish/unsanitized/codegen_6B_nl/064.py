
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Aur test cases jodo.
    """
    vowels = ''
    if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
        vowels += 1
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    s = count
    print (s)

if __name__=="__main__":
    s = '''

            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
            bbbbbbbbbbbbbbbbbbbbbbbbb    ccccccccccccccccccccccccccccccccccccccccccccccccccccc

            dddddddddddddddddddddddddddddddddddddddddccccccccccccccccccccccccccccccccccdddddd
            dddddddddddddddddddddddccccccccccccccccccccccccccccccccccccccccccccc

            ccccccccccccddddddddddddccccccccccccccccccccccccccccccdddd

            zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzeeeeeeeeeeecccceeecccccccccccccccccccccccccc
            zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzeeeeeeeeeeecc