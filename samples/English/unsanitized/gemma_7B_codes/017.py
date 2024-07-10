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
    count = 0
    beats = []
    for i in music_string:
        if i != ' ':
            count += 1
        else:
            beats.append(count)
            count = 0
    return beats


def sum_of_music(beats: List[int]) -> int:
    """
    Aapko ek list degi jo musical notes ko represent karti hai. Agar isme 3 note hain jisko o| .| o| se represent kiya ja raha hai,
    to wo ek integer ke aur ek float ke alag alag sum degi. Integer sum wo hai jo beat ke har ek element ka sum hai aur float
    sum wo hai jo beats ke har ek element ka average hai.

    >>> sum_of_music([4, 2, 1])
    ('6.00', '9.00')
    >>> sum_of_music([2, 2, 2, 2])
    ('8.00', '4.00')
    >>> sum_of_music([1, 2, 3, 4])
    ('10.00', '2.50')
    """
    sums = (sum(beats), int(float(sum(beats)) / len(beats)))
    return sums


if __name__ == "__main__":
    from doctest import testmod

    testmod()
