from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    t = ''
    t, res = a, ""
    for i, value in enumerate(a):
        value1 = t[i]
        value2 = b[i]
        value1 = str(ord(value1) ^ int(value2))
        res += value1
    return res


class Key:
    def __init__(self, n: int):
        self.elements: List[int] = []
        for i in range(n):
            self.elements.append(random.randint(0, 1))
        self.value = 1

    def add(self, a: int, b: int) -> None:
        self.elements.append(a)
        self.elements.append(b)

    def mul(self, a: int, b: int) -> int:
        self.elements.append(a)
        self.elements.append(b)
        return self.value

    def keys(self) -> List[int]:
        """ Returns a list of 10 random numbers. Use to randomize. """
        return random.sample(range(0, 10), 10)