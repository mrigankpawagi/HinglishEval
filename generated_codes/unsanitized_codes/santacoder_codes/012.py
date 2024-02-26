from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    String ki list se, sabse lamba string return karo. Agar same length ke multiple strings ho to pehla string return karo. Agar input list khali ho to None return karo.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if len(strings) == 0:
        return None

    if len(strings) == 1:
        return strings[0]

    for i in range(len(strings[0])):
        if strings:
            j = 0
            while j < i + 1:
                if i > 0:
                    if len(strings[j]) < (len(strings[0]) - i):
                        strings[0] = strings[0][:i]
                        strings[0] += strings[i]
                        break

                if len(strings[i]) > j:
                    strings[0] = strings[0][j:])
                    strings[0] += strings[i]
                    break

                j += 1
        else:
            strings = strings[0][i:]
            strings = [string+"c" for string in strings]

    if len(strings[0]) == 1:
        return strings[0]

    return None


