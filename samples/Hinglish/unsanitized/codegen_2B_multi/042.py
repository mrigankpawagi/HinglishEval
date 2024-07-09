def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    l = list(l)
    next(l)
    return [el + 1 for el in l]


class Solution:
    def solve(self, cipher: str) -> str:
        """
        @param cipher A string
        @return A string
        """
        num = dict()
        for char in cipher:
            if not char.isdigit():
                for i, el in enumerate(num):
                    if char != el:
                        num[i] = chr(ord(char) + ord("a") - 1)
                        break
                else:
                    pass
            else:
                num[ord(char) - ord("0")] = char
        for i in range(1, 25):
            if num[i] != chr(ord("a") + i - 1):
                num[i] = num[i]
                break
        return "".join(
            [
                chr(ord(char) - ord("0"))
                for char, el in num.items()
                if el != chr(ord("a") + ord("0") - 1)
            ]
        )
