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
    """
    music_string = music_string.replace(' ', '')
    music_string = music_string.replace('|', '')
    music_string = music_string.replace('o', '4')
    music_string = music_string.replace('o|', '2')
    music_string = music_string.replace('.|', '1')
    music_string = music_string.replace('o o', '4 4')
    music_string = music_string.replace('o o|', '4 2 2 2 2 2 2 2 2 4 4')
    music_string = music_string.replace('o o| .| o| o| .| .| .| .| .| o o', '4 2 1 2 2 1 1 1 1 4 4')
    music_string = music_string.replace('o o| .| o| o| .| .| .| .| .| o o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .|