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
    if music_string =='':
        return []

    last_char, bev_type = music_string.split("|")
    if len(bev_type.lower()) == 0:
        return []
    if len(bev_type.lower()) == 1:
        bev_len = 1
        return [bev_len]

    return [bev_len * int(bev_type.lower()) for beh in list(music_string)[1]]


