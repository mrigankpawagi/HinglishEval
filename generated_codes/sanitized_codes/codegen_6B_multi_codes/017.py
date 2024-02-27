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
    music_string = music_string.replace(" ", "")
    list_of_integers = []
    count = count = 0
    while count < len(music_string):
        if count != 0 and count != 1:
            if music_string[(count + 1)] == music_string[count]:
                list_of_integers.append(4)
                count += 1
            else:
                list_of_integers.append(2)
        elif music_string[count] == music_string[count + 1]:
            list_of_integers.append(1)
            count += 2
        else:
            list_of_integers.append(0)
            list_of_integers.append(4)
            count += 2
        count += 1
    return list_of_integers