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
    if "o" in music_string:
        result: List[int] = []
        beat_dict = {"o": 0, "o|": 1, ".": 2, ".": 2}
        for char in music_string:
            if char == ".":
                result[beat_dict[char]] = 1
                break
            beat_dict[char] += 1
        return result