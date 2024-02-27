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
    """ musical_notes: List[int] = []
    # List contains each beat, half and quater note, split by '->'
    # Return musical_notes is list contains following list of beat and half_note

    if music_string.count('.')!= 2:
        raise Exception('music_string is not 2, expected: "O" or "O |"')

    # find next beat and half note
    i = 1
    j = music_string.index('@')
    while j!= music_string.index('->') and i < len(music_string):
        next_beat = music_string[j: i]
        next_half_note = music_string[j + 1: i + 1]

        # break out of while loop so next chalta element is always four beats tak chalta hai
        if len(next_beat)!= 4:
 