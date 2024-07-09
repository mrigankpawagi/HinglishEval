from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # parse string to lists of char values (char values == index in list)
    notes = [x for x in music_string]
    length = 13
    nth = length
    prev_nth = length
    res = [length for i in range(nth)]
    index_in_str = 0
    for ind in range(len(res)):
        # check if char is a |
        char_value = ord(notes[index_in_str])
        if not (65 <= char_value <=90 or 97 <= char_value <= 122):
            while (65 <= ord(notes[index_in_str]) <=90 or ord(notes[index_in_str+1]) <=90.0 or ord(notes[index_in_str+2]) <=90.0):
                res[ind] = 1
                index_in_str += 1
                if not (65 <= ord(notes[index_in_str]) <=90 or ord(notes[index_in_str+1]) <=90.0 or ord(notes[index_in_str+2]) <=90.0):
                    break
            # check if char is a o/
            char_value = ord(notes[index_in_str])
            if not (90 <= char_value <=97 or ord(notes[index_in_str+1]) <=95 or ord(notes[index_in_str+2]) <=95):
                res[ind] = 1
                index_in_str += 1
