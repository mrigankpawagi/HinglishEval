from typing import List


def parse_music(music_string: str) -> List[int]:
    """
    Is function ka input ek string hai jo musical notes ko ek special ASCII format mein represent karta hai.
    Aapka kaam hai is string ko parse karna aur ek integers ki list return karna jo correspond karti hai ki har note kitne beats tak chalta hai.

    Yaha ek legend hai:
    'o' - whole note, jo four beats tak chalta hai
    'o|' - half note, jo two beats tak chalta hai
    '.|' - quater note, jo one beat tak chalta hai

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """ m, tempo = 0, 30 // 4

    result = []

    for char in music_string:

        if char == "o":
            result.append(m)
            m = 0
            result.append(1)
            continue

        tempo -= 5
        if tempo < 0:
            tempo = 0
        if tempo > 30:
            tempo = 30
        result.append(tempo)

        #        print(m * 40)
        m = m * 40

    return result

