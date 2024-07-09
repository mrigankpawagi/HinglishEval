

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    matches = string.replace('x', '').replace(' ', '').replace('\n', '').replace('_', '').replace(
        '-', ''
    ).split()
    return sum(map(len, matches))

class Solution(object):
    def __init__(self, wordlist: List[int], words: List[str]) -> None:
        self.wordlist = wordlist
        self.words = words

    def canPairs(self, x: int, y: int) -> bool:
        return len(list(chain.from_iterable(self.canPairsIter(i,j) for i,j in zip(x,y))))!= 0

    def canPairsIter(self, i: int, j: int) -> Iterator[Tuple[int, int]]:
        if i == -1:
            return
        if j == -1:
            yield  (i,j)
        self.check_pairs(*self.canPairs(i-1, j-1))

    def check_pairs(self, x: int, y: int) -> None:
        if x >= y:
            return
        if self.canPairs(x-1, y) and self.canPairs(x, y-1):
            yield (x-1, y-1)
        if self.canPairs(x-1, y) and self.canPairs(x, y-1):
            yield (x-1, y-1)
        if self.canPairs(x, y-1) and self.canPairs(x-1, y-1):
            yield (x-1, y-1)

    def findDistinctPairs(self, words: List[str]) -> List[List[str]]:
        pairs = []
        for w