

def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    "*** YOUR CODE HERE ***"

class OrderedSet:
    """A set of ordered elements; hashable, indexable, and possibly a list of unsorted elements."""

    def __init__(self, iterable=None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # maps elements to singletons: note that singletons are like the dict.
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self.map.keys()))

    def add(self, e):
        """Insert an element e in set.  Since 0 is inserted as the first element, it
        doesn't guarantee order.

        >>> s = OrderedSet()
        >>> s.add('d')
        >>> s.add('d')
        >>> s.add('c')
        >>> s.left._p
        <Element... b2c(d,c) at 0x0000021A917B34F8>
        """
        if e not in self.map:
            self.map[e] = e
            if len(self.map) > len(self._data):
                end[-1] = end[-1] * 3 + self._p
            end += [None, end, end]
        else:
            end = self.map[e]
            end[-1] = end[-1] * 3 + self._p

    def discard(self, e):
