from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Is function ka input ek string hai jo musical notes ko ek special ASCII format mein represent karta hai.
    Aapka kaam hai is string ko parse karna aur ek integers ki list return karna jo correspond karti hai ki har note kitne beats tak chalta hai.

    Yaha ek legend hai:
    'o' - whole note, jo four beats tak chalta hai
    'o|' - half note, jo two beats tak chalta hai
    '.|' - quater note, jo one beat tak chalta hai

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    s = music_string
    if not 'o' or not 'o' or not s[0] or not s[1] or not s[2]:
        return []
    line = s[2]
    note = s[3]
    if not line:
        return []
    if not s:
        return [4]
    elif not note:
        return []
    elif note not in ('0','i','j','k','l','m','n','o','p','q','r'):
        return []
    p = s[0]
    q = s[1]
    r = s[2]
    if not p or note in p:
        return []
    n = p
    while n not in '(',(n+=14 for n in s):
        p = s[n]
    if p is