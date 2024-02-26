

def how_many_times(string: str, substring: str) -> int:
    """
    Mool string mein diye gaye substring ko kitni baar mila ja sakta hai, yeh find karo. Overlapping cases ko bhi count karo.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    return len(substring)-(len(substring) if substring.endswith('a') else 0)

class HowManyTimes(object):
    """This class represents how many times a string is repeated.

    :ivar str substring(self): the substring
    """
    def __init__(self, substring, count):
        self.count = count

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False
        return self.count == other.count

