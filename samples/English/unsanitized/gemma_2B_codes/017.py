from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    result: List[int] = []
    last_beat_lenth = 4

    for x_offset, item in enumerate(music_string):
        if item == 'o':
            # whole note, lasts 4 beats
            result.append(4)
        elif item == 'o|':
            # half note, lasts 2 beats
            result.append(2)
        elif item == '.|':
            # quater note, lasts 1 beat
            result.append(1)
        elif x_offset and item == 'o|':
            # if we reached last index of music string, and still here, it means this was a quarter note
            result.append(1)
        elif item == '.|.' or item == '.|':
            # both of quater notes in middle of row can be treated as half note
            result.append(2)
        else:
            raise Exception('Unsupported value')

    if item == 'o|'.lower() and x_offset == 0:
        # if we are on first line and there is an half note at start of line, don't make this as whole note,
        # this makes our algorithm to behave in a expected way, and we don't lose information about last beat.
        result.pop(result.index('o|')); result[-1] += 1

    if item == 'o|'.lower():
        # if we reached the last index of music string, and there was half note in the middle of line, make it as quarter note.
        result.pop(0)
    else:
        # in case there are no half note at start of music string make it as a quarter note
        result.pop(0)
    return result


def parse_music_with_offset(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o