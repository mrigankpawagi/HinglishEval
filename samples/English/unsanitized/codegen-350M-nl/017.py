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
    return parse_music(music_string)


class Time:
    def __init__(self, d: str, i: int = 8, s: dict = {}, a: str = ''):
        self.d = d
        self.i = i
        self.s = s
        self.a = a
        self.__class__ = Time
        self.s__class = Time
        self.t = time

    def __reduce__(self) -> (int, Time) : 
        s = self.s
        s.update(self.a)
        s
        return (int(10), Time(d.replace("o"," | ")))
    __init__:
    @property
    def t(self) -> Time :
        return self.t
    t
x = Time(d.replace("o","|")).t
print(x)
x.t


class COUNT:
    def __init__(self) :
        self.b