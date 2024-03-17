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
    if music_string[2:] == '':
        return None

    music_string = music_string.strip()

    if len(music_string) < 4 or music_string[2:] == '':
        return None

    music_string = music_string[0:2] # remove 'o'from the beginning of each line.

    note_value = int(music_string)

    if note_value!= int(note_value) or music_string[0]!= 'o':
        return None

    music_note = music_string[1].strip('\'.|'.')

    if music_note == '|':

        note_value.append(1)
        note_value[-1] += 1
        return note_value

    elif music_note[0] == '.' or "^" in music_note:

        note_value[0] += 1

 