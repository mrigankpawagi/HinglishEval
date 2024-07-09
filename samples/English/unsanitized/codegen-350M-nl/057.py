

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return any(n in l for n in l)

  def hasEqual(self, a1, a2):
    """Equal two sets of elements.
    >>> hasEqual([[1, 2], [3, 4], [5, 6, 7], [8, 9, 10]])
    True
    """
    return any(a1 in a2 for a1 in a2)

  def equals(self, l: list):
    """Equal two lists.
    >>> equals([(1, 2), (3, 4, 5, 6), (7, 9, 10), (8, 9, 10, 0)]
    True
    >>> equals([(0, 1), (0, 2), (1, 3), (2, 4), (2, 5), (3, 4], 0)]
    True
    """
    return any(all(isinstance(a, List) for a in l) for a in l)

  def maxDifference(self, l: list):
    """Max-Difference.
    >>> maxDifference([[1, 2], [3, 4], [5, 6, 7]])
    7
    """
    return any(l in self for l in self)

  def reverse(self, l: list):
    """Reverse.
    >>> reverse([1, 2], 2)
    [1, 2, 4, 6]
    """
    return any(x in l for x in self for b in l)

  def unset(self, id: str):
    """Set a value without modifying the